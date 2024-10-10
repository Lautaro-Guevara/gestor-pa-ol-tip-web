
export function listaEmpleados(){
    // Lista Desplegable de Empleados
    fetch("/listado_personal")
        .then(response => response.json())
        .then(data => {
            const selection = document.querySelector("#seleccion-lp");
            if (selection) {
                data.forEach(persona => {
                    const opcion = document.createElement("option");
                    opcion.value = persona.LP;
                    opcion.innerHTML = `${persona.LP} - ${persona.Nombre} ${persona.Apellido}`;
                    selection.appendChild(opcion);
                });
            }
        })
        .catch(error => console.error('Error al cargar la lista de empleados:', error));
}
  

export function listaCategorias(){

    // Lista delplegable de Categorias de Inventario
    fetch("/stock/categorias") // Seleccionar la ruta
        .then(response => response.json())
        .then(data => {
            const selection = document.querySelector("#seleccion-categoria"); // Seleccionar el id de la etiqueta select

            if (selection) {
                data.forEach(categoria => {
                    const opcion = document.createElement("option");
                    opcion.value = categoria.nombre;
                    opcion.innerHTML = `${categoria.nombre}`;
                    selection.appendChild(opcion);
                });
            }
        })
        .catch(error => console.error('Error al cargar la lista de categorías:', error));
}
    
