document.addEventListener("DOMContentLoaded", function(){


    // Lista Desplegable de Empleados
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

    // Lista delplegable de Categorias de Inventario
    fetch("/stock/categorias") // Seleccionar la ruta
    .then(response => response.json())
    .then(data => {
        const selection = document.querySelector("#seleccion-categoria"); // Seleccionar el id de la etiqueta select

        data.forEach(categoria => { 
            const opcion = document.createElement("option")
            // Editar las propiedades de las etiquetas opcion que van a ser mostradas
            opcion.value = categoria.nombre // Valor de la opcion 
            opcion.innerHTML = `${categoria.nombre}`; // Texto con el que se vera la opcion
            selection.appendChild(opcion) // Insertar la opcion en la etiqueta select
        })

    });
});