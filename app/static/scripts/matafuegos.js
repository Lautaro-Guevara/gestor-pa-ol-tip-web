

document.addEventListener("DOMContentLoaded", function(){
    











    // Display tabla de matafuegos
    fetch("/matafuegos-lista")
    .then(response => response.json())
    .then(data => {
        const hoy = new Date()

        // celda 10kg - Disponible
        const celda10kgDisponible = document.getElementById("celda-10kg-disponible")
        celda10kgDisponible.innerHTML = ""
        let total10kgDisponible = 0

        // celda 5kg - Disponible
        const celda5kgDisponible = document.getElementById("celda-5kg-disponible")
        celda10kgDisponible.innerHTML = ""
        let total5kgDisponible = 0
        
        // celda 2.5kg - Disponible
        const celda25kgDisponible = document.getElementById("celda-2.5kg-disponible")
        celda25kgDisponible.innerHTML = ""
        let total25kgDisponible = 0

        // celda 1kg - Disponible
        const celda1kgDisponible = document.getElementById("celda-1kg-disponible")
        celda10kgDisponible.innerHTML = ""
        let total1kgDisponible = 0

        // celda 10kg - Vencido
        const celda10kgVencido = document.getElementById("celda-10kg-vencido")
        celda10kgVencido.innerHTML = ""
        let total10kgVencido = 0

        // celda 5kg - Vencido
        const celda5kgVencido = document.getElementById("celda-5kg-vencido")
        celda10kgVencido.innerHTML = ""
        let total5kgVencido = 0

        // celda 2.5kg - Vencido
        const celda25kgVencido = document.getElementById("celda-2.5kg-vencido")
        celda10kgVencido.innerHTML = ""
        let total25kgVencido = 0

        // celda 1kg - Vencido
        const celda1kgVencido = document.getElementById("celda-1kg-vencido")
        celda1kgVencido.innerHTML = ""
        let total1kgVencido = 0


        // Tabla Resumen
        const tbody = document.getElementById("tabla-matafuegos")
        tbody.innerHTML = "";



        data.forEach(matafuego => {


            const fechaVencimiento = new Date(matafuego.fecha_vencimiento)
            const año = fechaVencimiento.getFullYear();
            const mes = String(fechaVencimiento.getMonth()).padStart(2,"0");
            const dia = String(fechaVencimiento.getDate()).padStart(2,"0");
            const nuevaFechaVencimiento = `${dia}/${mes}/${año}`

            if (matafuego.capacidad_matafuego === "10 kg") {
                if (fechaVencimiento.getTime() >= hoy.getTime()) {
                total10kgDisponible = total10kgDisponible+1;
            }
            else{
                total10kgVencido = total10kgVencido+1
            };
            };

            if (matafuego.capacidad_matafuego === "5 kg") {
                if (fechaVencimiento.getTime() >= hoy.getTime()) {
                total5kgDisponible = total5kgDisponible+1;
            }
            else{
                total5kgVencido = total5kgVencido+1
            };
            };

            if (matafuego.capacidad_matafuego === "2.5 kg") {
                if (fechaVencimiento.getTime() >= hoy.getTime()) {
                total25kgDisponible = total25kgDisponible+1;
            }
            else{
                total10kgVencido = total10kgVencido+1
            };
            };

            if (matafuego.capacidad_matafuego === "1 kg") {
                if (fechaVencimiento.getTime() >= hoy.getTime()) {
                total1kgDisponible = total1kgDisponible+1;
            }
            else{
                total1kgVencido = total1kgVencido+1
            };
            };
            

            const fila = document.createElement("tr");
            fila.innerHTML = `
                <td>${matafuego.id_matafuego}</td>
                <td>${matafuego.capacidad_matafuego}</td>
                <td>${nuevaFechaVencimiento}</td>
                <td>${matafuego.ubicacion_actual_matafuego}</td>
            `;

            tbody.appendChild(fila)
        });
        

        celda10kgDisponible.innerHTML = `${total10kgDisponible}`
        celda10kgVencido.innerHTML = `${total10kgVencido}`

        celda5kgDisponible.innerHTML = `${total5kgDisponible}`
        celda5kgVencido.innerHTML = `${total5kgVencido}`

        celda25kgDisponible.innerHTML = `${total25kgDisponible}`
        celda25kgVencido.innerHTML = `${total25kgVencido}`

        celda1kgDisponible.innerHTML = `${total1kgDisponible}`
        celda1kgVencido.innerHTML = `${total1kgVencido}`
    })
})