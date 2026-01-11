document.addEventListener('DOMContentLoaded', function() {
    // Cargar datos de partidos
    fetch('/api/partidos')
        .then(response => response.json())
        .then(data => {
            // Actualizar la página según la URL
            if (window.location.pathname === '/') {
                actualizarClasificacion(data);
            } else if (window.location.pathname === '/calendario') {
                actualizarCalendario(data);
            }
            // Puedes añadir más condiciones para otras páginas
        })
        .catch(error => console.error('Error:', error));
});

function actualizarClasificacion(partidos) {
    const tabla = document.getElementById('tabla-clasificacion');
    if (!tabla) return;
    
    // Aquí iría la lógica para procesar los partidos y generar la clasificación
    // Esto es solo un ejemplo básico
    tabla.innerHTML = `
        <thead>
            <tr>
                <th>Equipo</th>
                <th>PJ</th>
                <th>PG</th>
                <th>PP</th>
                <th>PF</th>
                <th>PC</th>
                <th>Pts</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Equipo Ejemplo</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
                <td>0</td>
            </tr>
        </tbody>
    `;
}

function actualizarCalendario(partidos) {
    const contenedor = document.getElementById('lista-partidos');
    if (!contenedor) return;
    
    contenedor.innerHTML = '';
    
    for (const [id, partido] of Object.entries(partidos)) {
        const partidoElement = document.createElement('div');
        partidoElement.className = 'partido';
        partidoElement.innerHTML = `
            <h3>${partido.local.nombre} vs ${partido.visitante.nombre}</h3>
            <p>Jornada: ${partido.Jornada}</p>
        `;
        contenedor.appendChild(partidoElement);
    }
}