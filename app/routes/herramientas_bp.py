from flask import Blueprint, render_template, jsonify, url_for, request, redirect
import json
from app.models import HerramientasAPrestamo, HerramientasACargo, ControlDiario, Elementos, Personal
from app import db

herramientas_bp = Blueprint("herramientas", __name__)

@herramientas_bp.route('/herramientas-prestamo.html')
def herramientas_prestamo_page():
    return render_template('herramientas-prestamo.html')

@herramientas_bp.route("/herramientas-prestamo/prestamo", methods=["POST"])
def registrar_prestamo_herramientas():
    """

    """
    registros_json = request.form.get("registrosHerramientas")
    if not registros_json:
        return "No se recibieron datos", 400  # Agregar un mensaje de error si los datos no llegan correctamente
    
    registros = json.loads(registros_json)
    

    try:
        for registro in registros:


            nuevo_prestamo = HerramientasAPrestamo(
                legajo_personal = registro["legajo"],
                fecha = registro["fecha"],
                herramienta = registro["nombreElemento"],
                observaciones = registro["observaciones"]
            )



            db.session.add(nuevo_prestamo)
        
        db.session.commit()

        return redirect(url_for("herramientas.herramientas_prestamo_page"))


    except Exception as e:
        return f"Error al registrar: {str(e)}", 500
    

@herramientas_bp.route("/herramienta-prestamo/devolucion", methods=["POST"])
def devolucion_herramienta():
    """
    Recibir nombre elemento y legajo
    agregar valor en fecha devolucion donde las condiciones sean true
    """
    registros_json = request.form.get("registrosHerramientas")
    
    if not registros_json:
        return "No se recibieron datos", 400  # Agregar un mensaje de error si los datos no llegan correctamente
    
    registros = json.loads(registros_json)
    

    try:
        for registro in registros:

            legajo_personal = registro["legajo"]
            nombre_elemento = registro["nombreElemento"]
            fecha_devolucion = registro["fecha"]

            # Buscar el registro que coincida con legajo_personal y nombre_elemento
            herramienta_prestamo = HerramientasAPrestamo.query.filter(
                HerramientasAPrestamo.legajo_personal == legajo_personal,
                HerramientasAPrestamo.herramienta == nombre_elemento
            ).first()

            # Verificar si se encontró el registro
            if herramienta_prestamo:
                # Actualizar la fecha de devolución
                herramienta_prestamo.fecha_devolucion = fecha_devolucion
            else:
                # Si no se encontró el registro, manejar el error (opcional)
                return f"No se encontró el registro para el legajo {legajo_personal} y el elemento {nombre_elemento}", 404



            # Guardar los cambios en la base de datos
        db.session.commit()

        return redirect(url_for("herramientas.herramientas_prestamo_page"))

    except Exception as e:
        db.session.rollback()  # Rollback en caso de error
        return f"Error al registrar la devolución: {str(e)}", 500
    

@herramientas_bp.route("/herramienta-prestamo/historial", methods=["GET"])
def historial_herramientas_prestadas():

    historial = db.session.query(
        HerramientasAPrestamo.legajo_personal,
        HerramientasAPrestamo.fecha,
        HerramientasAPrestamo.herramienta,
        HerramientasAPrestamo.observaciones,
        HerramientasAPrestamo.fecha_devolucion,
        Personal.nombre,
        Personal.apellido
    ).join(Personal, HerramientasAPrestamo.legajo_personal == Personal.legajo_personal)\
    .all()
    

    #historial = HerramientasAPrestamo.query.all()

    prestamos = [{"legajo": prestamo.legajo_personal, "fecha": prestamo.fecha,"elemento": prestamo.herramienta,"observaciones":prestamo.observaciones,"fecha_devolucion": prestamo.fecha_devolucion, "nombre": prestamo.nombre,"apellido": prestamo.apellido} for prestamo in historial]

    
    

    return jsonify(prestamos)

@herramientas_bp.route("/herramienta-prestamo/adeudando", methods=["GET"])
def herramientas_adeudadas():

    legajo = request.args.get("legajo")
    
    if not legajo:
        return "Legajo no proporcionado", 400
    
    # Consultar herramientas que aun no han sido devueltas
    adeudadas = HerramientasAPrestamo.query.filter(HerramientasAPrestamo.legajo_personal == legajo,
    HerramientasAPrestamo.fecha_devolucion == None ).all()

    resultados = [
        {
            "legajo": prestamo.legajo_personal,
            "fecha": prestamo.fecha,
            "elemento": prestamo.herramienta,
            "observaciones": prestamo.observaciones
        }
        for prestamo in adeudadas
    ]

    return jsonify(resultados)


@herramientas_bp.route('/herramientas-cargo.html')
def herramientas_cargo_page():
    return render_template('herramientas-cargo.html')



@herramientas_bp.route("/herramientas-cargo/cargo", methods=["POST"])
def dejar_cargo_herramienta():

    registros_json = request.form.get("registros")

    
    if not registros_json:
        return "No se recibieron datos", 400  # Agregar un mensaje de error si los datos no llegan correctamente
    

    registros = json.loads(registros_json)

    try:
        for registro in registros:
            cantidad = registro.get("cantidad", 1)  # Por si acaso 'cantidad' no está presente
            
            for _ in range(int(cantidad)):
                registro_herramienta_a_cargo = HerramientasACargo(
                    legajo_personal=registro["legajoDestinatario"],
                    fecha_entrega=registro["fecha"],
                    herramienta=registro["elemento"],
                    id_herramienta=registro["numeroElemento"],
                    procedencia=registro["legajoProcedencia"],
                    observacion=registro["observaciones"]
                )
                db.session.add(registro_herramienta_a_cargo)

        db.session.commit()

        return redirect(url_for("herramientas.herramientas_cargo_page"))

    except Exception as e:
        db.session.rollback()  # Es una buena práctica hacer rollback en caso de error
        return f"Error al registrar: {str(e)}", 500
