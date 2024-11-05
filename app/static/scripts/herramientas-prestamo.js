import { listaEmpleados } from "./modulo-listas-desplegables.js";

document.addEventListener("DOMContentLoaded", function(){
    listaEmpleados();
    fetch('/herramienta-prestamo/historial')
    .then(response => response.json())
    .then(data => {
        const tbody = document.getElementById("historial-prestamo-herramientas");
        tbody.innerHTML = "";
        data.forEach(registro => {
            if (!registro.fecha_devolucion){
              const fechaRegistro = new Date(registro.fecha)
            const año = fechaRegistro.getFullYear();
            const mes = String(fechaRegistro.getMonth()+1).padStart(2,"0");
            const dia = String(fechaRegistro.getDate()+1).padStart(2,"0");
            const nuevaFechaRegistro = `${dia}/${mes}/${año}`
            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${nuevaFechaRegistro}</td>
                <td>${registro.elemento}</td>
                <td>${registro.legajo}</td>
                <td>${registro.apellido} - ${registro.nombre}</td>
                <td>${registro.observaciones}</td>
                <td>${registro.cantidad}</td>
                
            `;
            tbody.appendChild(fila)  
            }
            
        });
    });
});


const formulario = document.getElementById("form-herramientas-prestamo");
const casillaElemento = document.getElementById("casilla-elemento");
const seleccion = document.querySelectorAll("input[name='accion']");

// Añadir el evento a todos los radio buttons
seleccion.forEach(radio => {
    radio.addEventListener("change", function() {
        const accionSeleccionada = document.querySelector("input[name='accion']:checked").value;
        
        // Limpiar el contenido actual del cuerpo del formulario
        casillaElemento.innerHTML = "";

        if (accionSeleccionada === "entrega") {
            formulario.action = "/herramientas-prestamo/prestamo"
            // Si se selecciona "entrega", insertar el formulario correspondiente
            casillaElemento.innerHTML = `

                    <input type="text" id="nombre-elemento" name="nombre-elemento" placeholder="Especificar elemento..." >

            `;
        } else if (accionSeleccionada === "devolucion") {
            formulario.action = "/herramienta-prestamo/devolucion"
            // Si se selecciona "devolución", insertar otro contenido

            casillaElemento.innerHTML = "";

            casillaElemento.innerHTML = `

                    <select name="nombre-elemento" id="nombre-elemento">
                        <option value="" disabled selected>Escoge tu opcion...</option>
                        <!--Las opciones se cargan con js-->
                    </select>

            `

            const listaHerramientasPrestadas = document.getElementById("nombre-elemento");
            
            
            if (listaHerramientasPrestadas) {
                listaHerramientasPrestadas.addEventListener("click", function(){
                    listaHerramientasPrestadas.innerHTML = ""
                    const legajoSeleccionado = document.getElementById("seleccion-lp").value
                    // Lista delplegable de Categorias de Inventario
                    fetch(`/herramienta-prestamo/adeudando?legajo=${legajoSeleccionado}`) // Seleccionar la ruta
                    .then(response => response.json())
                    .then(data => {
                        data.forEach(prestamo => {
                            const opcion = document.createElement("option");
                            opcion.value = prestamo.elemento;
                            opcion.innerHTML = `${prestamo.elemento}`;
                            listaHerramientasPrestadas.appendChild(opcion);
                        });
                        
                    })
                    .catch(error => console.error('Error al cargar la lista de herramientas adeudadas:', error));
                })};
        }
        
    });
});


// Logica de carga de registros

// Obtener elementos




const observacionesInput = document.getElementById('observaciones');

// Botones
const agregarElementoBtn = document.getElementById("agregar-elemento") //  Boton para agregar elemento al conjunto de registro
const aceptarBtn = document.getElementById("aceptar") // Boton de confirmacion
const registrosHerramientas = [];  // Array para almacenar los registros
const detallesAgregados = document.getElementById('detalles-agregados');



agregarElementoBtn.addEventListener("click", function(){
    const legajoSelect = document.getElementById("seleccion-lp")
    const nombreElementoInput = document.getElementById('nombre-elemento');
    const cantidadInput = document.getElementById('cantidad');

    const legajo = legajoSelect.value;
    const fecha = fechaInput.value
    const nombreElemento = nombreElementoInput.value;
    const cantidad = cantidadInput.value;
    const observaciones = observacionesInput.value;

    // Validación básica de los campos
    if (!legajo || !nombreElemento || !cantidad) {
        alert('Por favor, completa todos los campos obligatorios.');
        return;
    }

    
        // Agregar el registro a la lista de registros
    registrosHerramientas.push({
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
    cantidadInput.value = '1';
    observacionesInput.value = '';
    console.log(registrosHerramientas)
    
});

// Función para enviar el formulario y los registros
aceptarBtn.addEventListener('click', function (event) {
    
    const legajoSelect = document.getElementById('seleccion-lp');
    const fechaInput = document.getElementById('fecha');
    const nombreElementoInput = document.getElementById('nombre-elemento');
    const cantidadInput = document.getElementById('cantidad');


    //errorMsg.textContent = '';

    if (registrosHerramientas.length === 0) {
        alert('Por favor, agrega al menos un elemento.');
        event.preventDefault();  // Evitar envío si no hay registros
        return;
    }

    
    const registrosInputHerramientas = document.createElement('input');
    registrosInputHerramientas.type = 'hidden';
    registrosInputHerramientas.name = 'registrosHerramientas'; // Nombre para acceder en Flask
    registrosInputHerramientas.value = JSON.stringify(registrosHerramientas); // Convertir el array a JSON
    document.getElementById('form-herramientas-prestamo').appendChild(registrosInputHerramientas);

    // Limpiar los campos después de registrar
    legajoSelect.value = "";
    fechaInput.value = today;
    nombreElementoInput.value = '';
    cantidadInput.value = '1';
    observacionesInput.value = '';
    registrosHerramientas = [];

});

