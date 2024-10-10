from flask import Blueprint, render_template, jsonify, url_for, request, redirect
import json
from app.models import Personal, ControlDiario, Elementos
from app import db  # Asegúrate de importar la instancia de db

entregas_diarias_bp = Blueprint("entregas-diarias", __name__)

@entregas_diarias_bp.route("/entregas-diarias.html")
def entregas_diarias():
    return render_template("entregas-diarias.html")

@entregas_diarias_bp.route("/entregas-diarias", methods=["POST"])
def registrar_entrega():
    # Capturar los registros y trasformarlos en formato JSON
    registros_json = request.form.get("registros")
    registros = json.loads(registros_json)
    
    try:

        # Iterar los registros
        for registro in registros:

            nombre_elemento = registro["nombreElemento"]

            elemento = Elementos.query.filter_by(nombre=nombre_elemento).first() #"Seleccionar el id donde el nombre elemento = nombre"
            
            if not elemento:
                return "Elemento no encontrado", 400
    
         # Capturar los datos del formulario
            nueva_entrega = ControlDiario(
                id_elemento = elemento.id_elementos,
                legajo_personal = registro["legajo"],
                cantidad = registro["cantidad"],
                fecha = registro["fecha"],
                comentarios = registro["observaciones"],
                id_matafuego = None,
                accion = "Retiro"
            )
            
            

            # Añadir a la base de datos
            db.session.add(nueva_entrega)

        db.session.commit()

            

        return redirect(url_for("entregas-diarias.entregas_diarias"))
        

    except Exception as e:
        db.session.rollback()
        return f"Error al registrar la entrega: {str(e)}", 500
    
@entregas_diarias_bp.route("/control-diario", methods = ["GET"])
def mostrar_entrega_diaria():

    resultados = db.session.query(
        ControlDiario.fecha,
        ControlDiario.legajo_personal,
        Personal.nombre,
        Personal.apellido,
        ControlDiario.accion,
        Elementos.nombre
    ).join(Personal, ControlDiario.legajo_personal == Personal.legajo_personal) \
    .join(Elementos, ControlDiario.id_elemento == Elementos.id_elementos) \
    .all()

    

    resultado_json = [
        {
            "fecha": r.fecha,
            "legajo_personal": r.legajo_personal,
            "nombre": r[2],
            "apellido": r.apellido,
            "accion": r.accion,
            "elemento_nombre": r[5]  # El nombre del elemento es el sexto campo en los resultados
        }
        for r in resultados
    ]
        

    return jsonify(resultado_json)