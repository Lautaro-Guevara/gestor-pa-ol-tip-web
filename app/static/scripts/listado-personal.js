

document.addEventListener('DOMContentLoaded', function () {
    fetch('/listado_personal')
    .then(response => response.json())
    .then(data => {
        const tbody = document.querySelector('#tabla-personal tbody');
        tbody.innerHTML = "";
        data.forEach(persona => {
            const fila = document.createElement('tr');
            fila.innerHTML = `
                <td>${persona.LP}</td>
                <td>${persona.Nombre}</td>
                <td>${persona.Apellido}</td>
            `;
            tbody.appendChild(fila);
        });
    });

    fetch("/listado_personal")
    .then(response => response.json())
    .then(data => {
        const selection = document.querySelector("#seleccion-lp");

        data.forEach(persona => {
            const opcion = document.createElement("option")
            opcion.value = persona.LP
            opcion.innerHTML = `${persona.LP} - ${persona.Nombre} ${persona.Apellido}`;
            selection.appendChild(opcion)
        })

    });

    // Ocular tarjeta de informacion personal hasta elegir legajo personal

    const selectLegajo = document.getElementById('seleccion-lp');
    const tarjetaPersonal = document.getElementById('tarjeta-personal');
    const tablasInformacionIndividual = document.getElementById('tablas-informacion-individual');

    // Escucha el evento de cambio en el select
    selectLegajo.addEventListener('change', function () {
        if (selectLegajo.value) {
            // Si el usuario ha seleccionado una opción válida, muestra los elementos
            tarjetaPersonal.classList.remove('oculto');
            tablasInformacionIndividual.classList.remove('oculto');
        } else {
            // Si el valor es vacío o no válido, oculta los elementos
            tarjetaPersonal.classList.add('oculto');
            tablasInformacionIndividual.classList.add('oculto');
        }
    });
    
});