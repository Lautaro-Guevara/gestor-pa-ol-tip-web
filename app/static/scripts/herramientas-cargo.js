import { listaEmpleados } from "./modulo-listas-desplegables.js";
import { fechaDefaultForm } from "./fecha-default.js";

// Inicializar listas desplegables y fechas predeterminadas
listaEmpleados("#lp-procedencia-entrega");
listaEmpleados("#lp-destinatario");
listaEmpleados("#lp-procedencia-devolucion");
fechaDefaultForm("#fecha-entrega");
fechaDefaultForm("#fecha-devolucion");

// Registros para almacenar datos
const registrosEntrega = [];
const registrosDevolucion = [];

// Función para manejar clics en botones de "Agregar"
function agregarRegistro(tipo) {
    const inputs = obtenerInputs(tipo);

    // Validar campos obligatorios
    if (!inputs.fecha || !inputs.legajoProcedencia || !inputs.elemento || !inputs.cantidad) {
        alert("Por favor, completa todos los campos obligatorios.");
        return;
    }

    const nuevoRegistro = {
        fecha: inputs.fecha,
        legajoProcedencia: inputs.legajoProcedencia,
        legajoDestinatario: inputs.legajoDestinatario || null,
        elemento: inputs.elemento,
        numeroElemento: inputs.numeroElemento || null,
        estadoElemento: inputs.estadoElemento || null,
        cantidad: inputs.cantidad,
        observaciones: inputs.observaciones || "",
    };

    // Guardar en el registro correspondiente
    if (tipo === "entrega") registrosEntrega.push(nuevoRegistro);
    if (tipo === "devolucion") registrosDevolucion.push(nuevoRegistro);

    // Mostrar detalle agregado
    mostrarDetalleAgregado(nuevoRegistro, tipo);

    // Limpiar campos después de agregar
    limpiarCampos(tipo);
}

// Función para obtener los inputs según el tipo
function obtenerInputs(tipo) {
    return {
        fecha: document.querySelector(`#fecha-${tipo}`).value,
        legajoProcedencia: document.querySelector(`#lp-procedencia-${tipo}`).value,
        legajoDestinatario: tipo === "entrega" ? document.querySelector("#lp-destinatario").value : null,
        elemento: document.querySelector(`#nombre-elemento-${tipo}`).value,
        numeroElemento: tipo === "entrega" ? document.querySelector("#numeracion-elemento").value : null,
        estadoElemento: tipo === "devolucion" ? document.querySelector("#estado-elemento").value : null,
        cantidad: document.querySelector(`#cantidad-${tipo}`).value,
        observaciones: document.querySelector(`#observaciones-${tipo}`).value,
    };
}

// Función para mostrar el detalle agregado en el DOM
function mostrarDetalleAgregado(registro, tipo) {
    const detallesAgregados = document.querySelector(`#detalles-agregados-${tipo}`);
    const nuevoDetalle = document.createElement("p");
    nuevoDetalle.textContent = `${registro.cantidad} - ${registro.elemento} - ${registro.numeroElemento || registro.estadoElemento || ""} - ${registro.observaciones}`;
    detallesAgregados.appendChild(nuevoDetalle);
}

// Función para limpiar los campos después de agregar
function limpiarCampos(tipo) {
    document.querySelector(`#nombre-elemento-${tipo}`).value = "";
    document.querySelector(`#cantidad-${tipo}`).value = "1";
    document.querySelector(`#observaciones-${tipo}`).value = "";
    if (tipo === "entrega") {
        document.querySelector("#numeracion-elemento").value = "";
    }
}

// Función para registrar datos al aceptar
function aceptarRegistros(tipo) {
    const registros = tipo === "entrega" ? registrosEntrega : registrosDevolucion;
    if (registros.length === 0) {
        alert("Por favor, agrega al menos un elemento.");
        return;
    }

    // Crear input oculto con el JSON
    const registrosInput = document.createElement("input");
    registrosInput.type = "hidden";
    registrosInput.name = "registros";
    registrosInput.value = JSON.stringify(registros);

    document.querySelector(`#form-herramientas-cargo-${tipo}`).appendChild(registrosInput);

    // Limpiar registros después de aceptar
    limpiarCampos(tipo);
    if (tipo === "entrega") registrosEntrega.length = 0;
    if (tipo === "devolucion") registrosDevolucion.length = 0;
}

// Event listeners
document.addEventListener("DOMContentLoaded", () => {
    document.querySelector("#agregar-elemento-entrega").addEventListener("click", () => agregarRegistro("entrega"));
    document.querySelector("#agregar-elemento-devolucion").addEventListener("click", () => agregarRegistro("devolucion"));
    document.querySelector("#aceptar-entrega").addEventListener("click", () => aceptarRegistros("entrega"));
    document.querySelector("#aceptar-devolucion").addEventListener("click", () => aceptarRegistros("devolucion"));
});



