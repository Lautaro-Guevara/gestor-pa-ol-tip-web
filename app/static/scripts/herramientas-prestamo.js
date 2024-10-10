import { listaEmpleados } from "./modulo-listas-desplegables.js";

document.addEventListener("DOMContentLoaded", function(){
    listaEmpleados();
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
            formulario.action = "/herramientas-prestamo/devolucion"
            // Si se selecciona "devolución", insertar otro contenido

            casillaElemento.innerHTML = "";

            casillaElemento.innerHTML = `

                    <select name="nombre-elemento" id="nombre-elemento">
                        <option value="" disabled selected>Escoge tu opcion...</option>
                        <!--Las opciones se cargan con js-->
                    </select>

            `

            const listaHerramientasPrestadas = document.getElementById("nombre-elemento");
            const legajoSeleccionado = document.getElementById("seleccion-lp").value
            console.log(legajoSeleccionado)

            listaHerramientasPrestadas.addEventListener("click", function(){

                // Lista delplegable de Categorias de Inventario
                fetch(`/herramienta-prestamo/adeudando?legajo=${legajoSeleccionado}`) // Seleccionar la ruta
                .then(response => response.json())
                .then(data => {
                    

                    if (listaHerramientasPrestadas) {
                        data.forEach(prestamo => {
                            const opcion = document.createElement("option");
                            opcion.value = prestamo.elemento;
                            opcion.innerHTML = `${prestamo.elemento}`;
                            listaHerramientasPrestadas.appendChild(opcion);
                        });
                    }
                })
                .catch(error => console.error('Error al cargar la lista de herramientas adeudadas:', error));
            });
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
    
    console.log(registrosHerramientas)


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
    registros = []

});



