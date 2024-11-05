from flask import Blueprint, render_template, jsonify
import json
from app.models import Matafuegos
from app import db

matafuegos_bp = Blueprint("matafuegos", __name__)

@matafuegos_bp.route('/matafuegos.html')
def matafuegos():
    return render_template('matafuegos.html')

@matafuegos_bp.route("/matafuegos-lista", methods=["GET"])
def mostrar_lista_matafuegos():

    resultados = Matafuegos.query.all()

    matafuegos = [{
        "id_matafuego": matafuego.id_matafuego,
        "fecha_ingreso": matafuego.fecha_ingreso,
        "capacidad_matafuego": matafuego.capacidad_matafuego,
        "fecha_vencimiento": matafuego.fecha_vencimiento,
        "fecha_vencimiento_prueba_hidraulica": matafuego.fecha_vencimiento_prueba_hidraulica,
        "ubicacion_actual_matafuego": matafuego.ubicacion_actual_matafuego,
        "ubicacion_anterior_matafuego": matafuego.ubicacion_anterior_matafuego,
        "fecha_ultimo_movimiento": matafuego.fecha_ultimo_movimiento,
        "despresurizado": matafuego.despresurizado
    } for matafuego in resultados]

    return jsonify(matafuegos)

@matafuegos_bp.route('/matafuegos-paginas/movimiento-matafuego.html')
def pagina_historial_matafuegos():
    return render_template('matafuegos-paginas/movimiento-matafuego.html')