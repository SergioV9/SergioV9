from flask import Flask, jsonify, request, render_template 
import json
import os

app = Flask(__name__)

DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
DATA_FILE = os.path.join(DATA_DIR, 'partidos.json')
os.makedirs(DATA_DIR, exist_ok=True)

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def generar_calendario(equipos):
    # 1. Agrupar equipos por bombo y ordenar
    bombos = {}
    for equipo in equipos:
        bombo = equipo["bombo"]
        bombos.setdefault(bombo, []).append(equipo)
    # Ordenamos los equipos de cada bombo por nombre (puedes ajustar el criterio)
    for bombo in bombos:
        bombos[bombo].sort(key=lambda e: e["nombre"])
    bombos = dict(sorted(bombos.items(), key=lambda x: x[0]))
    
    # 2. Verificar que todos los bombos tengan la misma cantidad de equipos
    n = len(next(iter(bombos.values())))
    if any(len(lista) != n for lista in bombos.values()):
        raise ValueError("Todos los bombos deben tener la misma cantidad de equipos")
    
    # 3. Generar la lista de todos los partidos posibles 
    # (cada equipo se enfrenta a todos los equipos de los otros bombos)
    all_matches = []
    bombo_keys = list(bombos.keys())
    for i in range(len(bombo_keys)):
        for j in range(i+1, len(bombo_keys)):
            for equipo1 in bombos[bombo_keys[i]]:
                for equipo2 in bombos[bombo_keys[j]]:
                    all_matches.append((equipo1, equipo2))
    
    # 4. La cantidad mínima de jornadas es: (bombos - 1) * (equipos por bombo)
    total_rounds = (len(bombos) - 1) * n
    # El conjunto total de equipos (identificados por su nombre)
    teams_set = set(e["nombre"] for e in equipos)

    # Función auxiliar para encontrar, en la lista de partidos disponibles, un emparejamiento perfecto (ronda)
    def encontrar_ronda(match_list, equipos_disponibles):
        if not equipos_disponibles:
            return []  # se han emparejado todos
        # Tomamos el primer equipo (según orden alfabético de nombres)
        first = min(equipos_disponibles)
        for match in match_list:
            nombres_match = {match[0]["nombre"], match[1]["nombre"]}
            # Si 'first' está en el partido y ambos equipos están disponibles
            if first in nombres_match and nombres_match.issubset(equipos_disponibles):
                # Removemos los dos equipos del conjunto de disponibles
                nuevos_equipos = equipos_disponibles - nombres_match
                # Filtrar los partidos descartando aquellos que involucren alguno de estos equipos
                nuevos_match_list = [m for m in match_list if m[0]["nombre"] not in nombres_match and m[1]["nombre"] not in nombres_match]
                submatching = encontrar_ronda(nuevos_match_list, nuevos_equipos)
                if submatching is not None:
                    return [match] + submatching
        return None

    # 5. Backtracking para descomponer TODOS los partidos en rondas (jornadas) sin solapamientos.
    rounds_result = []
    # Usamos una copia de la lista de partidos disponibles.
    remaining_matches = all_matches.copy()

    def backtrack(remaining, rounds_so_far):
        # Si ya se han asignado todas las jornadas requeridas y no hay partidos pendientes, ¡éxito!
        if not remaining and len(rounds_so_far) == total_rounds:
            return rounds_so_far
        # Si ya se alcanzó el número de jornadas pero aún sobran partidos, falla esta rama
        if len(rounds_so_far) == total_rounds:
            if remaining:
                return None
            else:
                return rounds_so_far
        # Intentar generar una nueva ronda (jornada) a partir de los partidos restantes.
        ronda = encontrar_ronda(remaining, teams_set)
        if ronda is None:
            return None  # no se encontró una ronda válida: se retrocede
        # Eliminamos de la lista de partidos pendientes los partidos ya usados en la ronda
        nueva_lista = [m for m in remaining if m not in ronda]
        rounds_so_far.append(ronda)
        result = backtrack(nueva_lista, rounds_so_far)
        if result is not None:
            return result
        rounds_so_far.pop()
        return None

    schedule = backtrack(remaining_matches, [])
    if schedule is None:
        raise Exception("No se pudo generar un calendario válido.")
    
    # 6. Opcionalmente se podría reordenar las jornadas para que sigan un patrón de rotación
    # (por ejemplo: iniciar cada jornada con el bombo A, luego B, luego C, etc.).
    # En este ejemplo se conserva el orden obtenido por el backtracking.
    
    # 7. Formatear la salida en JSON (igual que en el código original)
    calendario_json = {}
    partido_id = 1
    for jornada_index, ronda in enumerate(schedule, start=1):
        for match_index, match in enumerate(ronda):
            # Alternar localía según número de jornada + posición del partido
            if (jornada_index + match_index) % 2 == 0:
                local, visitante = match
            else:
                visitante, local = match  # intercambio
            partido = {
                "Jornada": str(jornada_index),
                "Playoffs": "no",
                "eliminatoria": "",
                "numPartido": "",
                "puntosLocal": 0,
                "puntosVisitante": 0,
                "local": {
                    "nombre": local["nombre"],
                    "grupo": local["grupo"],
                    "bombo": local["bombo"],
                    "jugadores": {}
                },
                "visitante": {
                    "nombre": visitante["nombre"],
                    "grupo": visitante["grupo"],
                    "bombo": visitante["bombo"],
                    "jugadores": {}
                }
            }
            clave = f"Partido{partido_id}"
            calendario_json[clave] = partido
            partido_id += 1
    return calendario_json

# Rutas Flask (se mantienen iguales)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendario')
def calendario():
    partidos = load_data()
    return render_template('calendario.html', partidos=partidos)

@app.route('/estadisticas')
def estadisticas():
    partidos = load_data()
    return render_template('estadisticas.html', partidos=partidos)

@app.route('/playoffs')
def playoffs():
    partidos = load_data()
    return render_template('playoffs.html', partidos=partidos)

@app.route('/crearCalendario')
def crear_calendario():
    return render_template('crearCalendario.html')

@app.route('/api/partidos', methods=['GET'])
def get_partidos():
    return jsonify(load_data())

@app.route('/api/generar_calendario', methods=['POST'])
def api_generar_calendario():
    data = request.get_json()
    calendario = generar_calendario(data["equipos"])
    save_data(calendario)
    return jsonify({"success": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
