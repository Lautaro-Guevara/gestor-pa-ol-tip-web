
document.addEventListener('DOMContentLoaded', function () {
    const fechaHoraElement = document.getElementById('fecha-hora');
    
    function actualizarFechaHora() {
        const ahora = new Date();
        const opciones = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
        fechaHoraElement.textContent = ahora.toLocaleDateString('es-ES', opciones);
    }

    // Actualizar la fecha y hora cada minuto
    actualizarFechaHora();
    setInterval(actualizarFechaHora, 60000);
});
