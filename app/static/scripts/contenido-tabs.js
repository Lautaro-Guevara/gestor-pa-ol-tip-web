export function contenidoTabEpp() {
    const tab = document.querySelector("#contenido-tab-epp");

    fetch("/stock/categorias") // Ruta para conseguir categorías y subcategorías de EPP
        .then(response => response.json())
        .then(data => {
            if (tab) {
                // Convertir lista plana en un árbol
                const categoriasTree = construirArbolCategorias(data, 1); // 1 es el ID raíz
                tab.appendChild(crearHtmlArbol(categoriasTree, 1)); // Iniciar con nivel 1
                
                // Agregar event listener para delegar los clics en botones de agregar/quitar
                //tab.addEventListener('click', manejarClickBotones);

                

                
                
            }
        })
        .catch(error => console.error("Error al cargar la lista de EPP:", error));
}

// Función para construir un árbol de categorías desde una lista plana
function construirArbolCategorias(data, idPadre) {
    return data
        .filter(categoria => categoria.id_padre === idPadre)
        .map(categoria => {
            return {
                ...categoria,
                hijos: construirArbolCategorias(data, categoria.id_categoria)
            };
        });
}

// Función recursiva para crear el HTML del árbol de categorías
function crearHtmlArbol(categorias, nivel) {
    const fragment = document.createDocumentFragment();

    categorias.forEach(categoria => {
        if (categoria.hijos && categoria.hijos.length > 0) {
            // Si la categoría tiene hijos, crear <details> con la clase subcategoria{nivel}
            const details = document.createElement("details");
            details.className = `subcategoria${nivel}`; // Asignar clase basada en el nivel
            details.innerHTML = `<summary>${categoria.nombre}</summary>`;
            details.appendChild(crearHtmlArbol(categoria.hijos, nivel + 1)); // Llamada recursiva para hijos con nivel + 1
            fragment.appendChild(details);
        } else {
            // Si la categoría es una hoja, usar <div> con la clase subcategoria{nivel}
            const hoja = document.createElement("div");
            hoja.className = `subcategoria${nivel} hoja`;
            hoja.innerHTML = `
                <p>${categoria.nombre}</p>
                <button type="button" class="btn-agregar" data-nombre="${categoria.nombre}" padre="${categoria}">+</button>
                <button type="button" class="btn-quitar" data-nombre="${categoria.nombre}">-</button>
            `;
            fragment.appendChild(hoja);
        }
    });

    return fragment;
}






export function manejarClickBotones(event) {
    const target = event.target;

    if (target.classList.contains('btn-agregar')) {
        const nombreElemento = target.getAttribute('data-nombre');
        console.log("Se ha agregado", nombreElemento);
        const json = [{
            "accion": "agregar",
            "elemento": nombreElemento
        }];

        
        return json
    }

    if (target.classList.contains('btn-quitar')) {
        const nombreElemento = target.getAttribute('data-nombre');
        
        const json = [{
            "accion": "eliminar",
            "elemento": nombreElemento
        }];

        
        return json
    }


}