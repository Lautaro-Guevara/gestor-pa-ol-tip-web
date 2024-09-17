document.addEventListener('DOMContentLoaded', function () {
    // Obtener los elementos del DOM
    const agregarElementoBtn = document.getElementById('agregar-elemento');
    const aceptarBtn = document.getElementById('aceptar');
    const detallesAgregados = document.getElementById('detalles-agregados');
    const legajoSelect = document.getElementById('seleccion-lp');
    const fechaInput = document.getElementById('fecha');
    const nombreElementoInput = document.getElementById('nombre-elemento');
    //const inputOtros = document.getElementById('input-otros');
    const cantidadInput = document.getElementById('cantidad');
    //const otrosCheckbox = document.getElementById('otros-checkbox');
    const observacionesInput = document.getElementById('observaciones');
    const registros = [];  // Array para almacenar los registros
    
    const errorMsg = document.createElement('p');
    errorMsg.style.color = 'red';

    // Establecer la fecha actual por defecto
    const today = new Date().toISOString().split('T')[0];
    fechaInput.value = today;

    // Manejar la visibilidad del input "Otros"
    // otrosCheckbox.addEventListener('change', function () {
    //     if (otrosCheckbox.checked) {
    //         nombreElementoSelect.classList.add('oculto');
    //         inputOtros.classList.remove('oculto');
    //     } else {
    //         nombreElementoSelect.classList.remove('oculto');
    //         inputOtros.classList.add('oculto');
    //     }
    // });

    // Función para agregar un nuevo registro
    agregarElementoBtn.addEventListener('click', function () {
        const legajo = legajoSelect.value;
        const fecha = fechaInput.value
        const nombreElemento =  nombreElementoInput.value;
        const cantidad = cantidadInput.value;
        const observaciones = observacionesInput.value;

        // Validación básica de los campos
        if (!legajo || !nombreElemento || !cantidad) {
            alert('Por favor, completa todos los campos obligatorios.');
            return;
        }

        // Agregar el registro a la lista de registros
        registros.push({
            legajo: legajo,
            fecha: fecha,
            nombreElemento: nombreElemento,
            cantidad: cantidad,
            observaciones: observaciones
        });

        // Mostrar el registro en el globo de detalles agregados
        const nuevoDetalle = document.createElement('p');
        nuevoDetalle.textContent = `Elemento: ${nombreElemento}, Cantidad: ${cantidad}, Observaciones: ${observaciones}`;
        detallesAgregados.appendChild(nuevoDetalle);

        // Limpiar los campos después de agregar
        nombreElementoInput.value = '';
        //inputOtros.value = '';
        cantidadInput.value = '1';
        observacionesInput.value = '';
    });

    // Función para enviar el formulario y los registros
    aceptarBtn.addEventListener('click', function (event) {
        errorMsg.textContent = '';

        if (registros.length === 0) {
            alert('Por favor, agrega al menos un elemento.');
            event.preventDefault();  // Evitar envío si no hay registros
            return;
        }

        // Crear un campo oculto con los registros en formato JSON
        const registrosInput = document.createElement('input');
        registrosInput.type = 'hidden';
        registrosInput.name = 'registros';
        registrosInput.value = JSON.stringify(registros);
        document.getElementById('form-entrega-diaria').appendChild(registrosInput);

        detallesAgregados.innerHTML = "";

        // Limpiar los campos después de registrar
        legajoSelect.value = "";
        fechaInput.value = today;
        nombreElementoInput.value = '';
        cantidadInput.value = '1';
        observacionesInput.value = '';
        registros = []
    });
    
    
});

