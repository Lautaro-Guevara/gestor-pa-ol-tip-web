from flask import Blueprint, render_template, jsonify
from app.models import Personal

lista_personal_bp = Blueprint("lista_personal", __name__)

@lista_personal_bp.route('/listado-personal.html')
def listado_personal_page():
    return render_template('listado-personal.html')


@lista_personal_bp.route('/listado_personal', methods=['GET'])
def obtener_datos():
    
    lista_personal = Personal.query.all()
    
    
    empleados = [{"LP": persona.legajo_personal, "Nombre": persona.nombre, "Apellido": persona.apellido} for persona in lista_personal]
    
    return jsonify(empleados)