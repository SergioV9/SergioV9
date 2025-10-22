# 🏀 Gestor de Torneos de Baloncesto

## 📋 Descripción del Proyecto

Aplicación web local desarrollada en Python para gestionar torneos de baloncesto. Permite organizar ligas y playoffs completos al estilo NBA, con seguimiento detallado de estadísticas de jugadores y equipos.

## 🎯 Motivación

Creé esta aplicación porque el videojuego que usaba con mi familia no permitía organizar torneos personalizados a nuestro gusto. Esta solución permite crear el seguimiento de esos torneos que hago con mi padre y mi hermano, de una manera automatizada que facilita mucho la creación de futuros torenos. Esto es gracias a que es capaç de crear un calendario de partidos, una tabla de clasificación y de Playoffs y unas estadisticas detalladas con tan solo unos mínimos datos introducidos por el ususario. De esta manera ya podemos jugar a nuestro gusto y hacer una gestión del torneo personalizada.

## ⚙️ Funcionalidades Principales

### 🏆 Gestión de Torneos
- **Creación de Grupos:** Distribución automática de equipos en grupos
- **Calendario de Partidos:** Generación automática de todos los partidos para la fase de liga
- **Seguimiento de estadísticas:** Seguimiento completo de estadísticas de tanto equipos como jugadores
- **Sistema de Playoffs:** Asignación automática de los mejores equipos en su cuadrante
- **Resultados en Tiempo Real:** Actualizaciónes automáticas de clasificación, estadisticas y cuadrantes de playoffs despues de introducir los datos de cada partido
  
### 🌐 Interfaz Web
- **Navegación Intuitiva:** Diferentes secciones para cada funcionalidad
    - 1ª pestaña: Clasificación de los equipos
    - 2ª pestaña: Calendario de partidos
    - 3ª pestaña: Estadisticas detalladas de equipo y jugadores
    - 4ª pestaña: Cuadro de playoffs
- **Visualización de Datos:** Presentación clara de todos los datos

## 🛠 Stack Tecnológico
- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python
- **Almacenamiento:** JSON

## 🚀 Instalación y Uso

### Como usar
- **Introducir equipos:**
  - Lo primero de todo es introducir los equipos que jugaran este torneo, para ello nos dirigimos a la pestaña de calendario y le damos a "Crear Nuevo Calendario" (esto borrara todos los datos, si hay alguno, del torneo, así que primero asegurate que no te importa perderlos o copiales en otra parte)
  - A la hora de introducir los datos te pedira 3 datos para cada equipo;
    - Nombre: Este es el nombre del equipo
    - Grupo: El grupo al que pertenecerá el equipo (usa A y B si quieres hacer playoffs mas adelante)
    - Bombo: Los equipos que esten en el mismo bombo no jugaran entre ellos. Esto se usa para que a la hora de crear los rivales de mis diferentes equipos, estos no jueguen entre ellos y solo aparezcan enfrentamiento contra los equipos de mis rivales
    - Extra: si quieres que en la pestaña de playoffs aparazcan los equipos con sus escudos, engancha las fotos con el nombre del equipo y extensión .jpg en la carpeta de img (ya hay varios escudos que vienen en el proyecto, solo pon aquellos equipos que aparazcan sin su escudo)
  - Una vez introducidos todos los datos de todos los equipos que juegan, confirmalos y ya estas listo para empezar a disfrutar del torneo
- **Introducir datos de partido:**
  - 

### Prerrequisitos
- Ninguno, ya que no usa ninguna dependencia.

### Ejecución
```bash
# Descargar el proyecto
cd torneoBasquet NBA

# Ejecutar la aplicación
python app.py
