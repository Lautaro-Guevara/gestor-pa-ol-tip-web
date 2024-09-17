
document.addEventListener("DOMContentLoaded", function(){

    const fechaInput = document.getElementById('fecha');
    const today = new Date().toISOString().split('T')[0];
    fechaInput.value = today;

    fechaInput.addEventListener("change", function(){
        fetch("/control-diario")
    .then(response => response.json())
    .then(data =>{
        const tbody = document.querySelector("#movimiento-diario tbody");
        tbody.innerHTML = "";
        data.forEach(registro => {
            
            const fechaRegistro = new Date(registro.fecha)

            const año = fechaRegistro.getFullYear();
            const mes = String(fechaRegistro.getMonth()+1).padStart(2,"0");
            const dia = String(fechaRegistro.getDate()+1).padStart(2,"0");

            const nuevaFechaRegistro = `${año}-${mes}-${dia}`
            console.log(nuevaFechaRegistro)
            console.log(fechaInput.value)
            if (nuevaFechaRegistro == fechaInput.value){
                

            
                const fila = document.createElement("tr");
                fila.innerHTML = `
                    <td>${registro.legajo_personal}</td>
                    <td>${registro.apellido} - ${registro.nombre}</td>
                    <td>${registro.accion}</td>
                    <td>${registro.elemento_nombre}</td>
                    <td>${registro.para}</td>
                `;
                tbody.appendChild(fila);
            };
                
            
        });
    });
    })
    

    fetch("/control-diario")
    .then(response => response.json())
    .then(data =>{
        const tbody = document.querySelector("#movimiento-diario tbody");
        tbody.innerHTML = "";
        data.forEach(registro => {
            
            const fechaRegistro = new Date(registro.fecha)

            const año = fechaRegistro.getFullYear();
            const mes = String(fechaRegistro.getMonth()+1).padStart(2,"0");
            const dia = String(fechaRegistro.getDate()+1).padStart(2,"0");

            const nuevaFechaRegistro = `${año}-${mes}-${dia}`
            console.log(nuevaFechaRegistro)
            console.log(fechaInput.value)
            if (nuevaFechaRegistro == fechaInput.value){
                

            
                const fila = document.createElement("tr");
                fila.innerHTML = `
                    <td>${registro.legajo_personal}</td>
                    <td>${registro.apellido} - ${registro.nombre}</td>
                    <td>${registro.accion}</td>
                    <td>${registro.elemento_nombre}</td>
                    <td>${registro.para}</td>
                `;
                tbody.appendChild(fila);
            };
                
            
        });
    });


});