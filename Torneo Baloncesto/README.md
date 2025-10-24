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
- **Explicación rápida:**
  - Solo consta de dos pasos:
    - Introducción de equipos para que se cree la clasificación de los grupos y el calendario
    - Actualización de los resultados de los partido para que el torneo vaya avanzando hacia su desenlace
- **Introducir equipos:**
  - Lo primero de todo es introducir los equipos que jugaran este torneo, para ello nos dirigimos a la pestaña de calendario y le damos a "Crear Nuevo Calendario" (esto borrara todos los datos, si hay alguno, del torneo, así que primero asegurate que no te importa perderlos o copiales en otra parte)
  - A la hora de introducir los datos te pedira 3 datos para cada equipo;
    - Nombre: Este es el nombre del equipo
    - Grupo: El grupo al que pertenecerá el equipo (usa A y B si quieres hacer playoffs mas adelante)
    - Bombo: Los equipos que esten en el mismo bombo no jugaran entre ellos. Esto se usa para que a la hora de crear los rivales de mis diferentes equipos, estos no jueguen entre ellos y solo aparezcan enfrentamiento contra los equipos de mis rivales
    - Extra: si quieres que en la pestaña de playoffs aparazcan los equipos con sus escudos, engancha las fotos con el nombre del equipo y extensión .jpg en la carpeta de img (ya hay varios escudos que vienen en el proyecto, solo pon aquellos equipos que aparazcan sin su escudo)(esto se puede hacer en cualquier momento)
  - Una vez introducidos todos los datos de todos los equipos que juegan, confirmalos y ya estas listo para empezar a disfrutar del torneo
- **Introducir datos de partido:**
  - Los datos se pueden introducir de dos maneras
    - 1ª: Poner SOLO el RESULTADO del partido: Esta opción es la mas fácil y la mas rápida pero de esta manera no habrá estadísticas de equipo ni de jugadores. Si tu eres una persona que las estadísticas no las miras o que quieres jugar un torneo rápido con todas las opciones (clasificación, calendario y playoffs) menos la pestaña de estadisticas, esta es tu mejor opción.
      - Para esto solamente has de abrir el documento partidos.json y encontrar el partido que has jugado (estan ordenados en orden) y poner el resultado de cada equipo en su respectiva variable (puntosLocal o puntosVisitante)
    - 2ª: Poner los DATOS del partido COMPLETOS: Esta opción es más larga pero te permite disfrutar de todas las características de este proyecto. Esto se puede hacer de dos maneras, una con IA (muy recomendado ya que te quita mucho trabajo) y otra introduciendo los datos a mano (que puede hacerse un poco pesado)
      - Introducir DATOS CON IA: En este caso es importante tener en cuenta el archivo read.txt dentro del proyecto donde esta el script que hay que pasarle a la IA para que te haga el codigo que se necesita para el json (IMPORTANTE leerse la parte escrita ya que hay que hacer un par de pequeños cambios).
        - Una vez ya le hayamos pasado el script ya podemos empezar a pasarle los datos de los partidos en este mismo chat.
        - Los datos del partido seran en un formato de foto ya que es lo más rápido y fácil (la foto se ha de sacar al acabar el partido del juego, donde el propio juego te muestra las estadísticas de un equipo y otro) y se enviaran junto con 4 datos puestos a mano ({el numero del partido}, {el atributo jornada}, {nombre del equipo local}, {nombre del equipo visitante}) que obviamente son diferentes por cada partido y estos se encuentran en el json (se tiene que buscar en el json, el encuentro de ese mismo partido donde estarán los 4 atributos que buscamos).
        - Una vez que ya le hayas pasado las fotos de los datos de los equipos y los 4 datos, la IA empezará a generar el codigo json para nuestro partido en específico, que tendra que ser reemplazado por el código de nuestro mismo partido en nuestro archivo json (ya que este no tiene los valores).
        - REPASO RÁPIDO:
          - Copiar el script (haciendo las modificaciones necesarias) (Este es el pimer prompt a enviar)
          - Hacer la foto a las estadísticas de los jugadores al acabar de jugar el partido y encontrar en el json los 4 atributos necesarios del partido que le vamos a pasar las fotos para que la IA pueda generar el codigo entero
          - Sustituir el codigo que nos a proporcionado la IA por el nuestro (que esta sin datos del partido) en nuestro json
      - Introducir datos MANUALMENTE: Esta opción no necesita IA ya que los datos los pones tu modificando el propio archivo json. Para esto solo has de encontrar el partido que se ha jugado y ir cambiando los datos de los equipos y jugadores uno por uno, si lo haces de esta manera puedes escoger que estadisticas poner y cuales no (ya que ponerlas todas puede llevarte un tiempo). Es recomendable probar la otra opción primero ya que te ahorrara mucho tiempo

### Prerrequisitos
- Ninguno, ya que no usa ninguna dependencia.

### Ejecución
```bash
# Descargar el proyecto
cd torneoBasquet NBA

# Ejecutar la aplicación
python app.py
