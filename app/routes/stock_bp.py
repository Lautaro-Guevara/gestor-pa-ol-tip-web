from flask import Blueprint, jsonify
from app.models import CategoriasInventario

stock_bp = Blueprint("stock",__name__)


@stock_bp.route("/stock/categorias", methods=['GET'])
def mostrar_categorias():
    lista_categorias = CategoriasInventario.query.all()

    categorias = [{"nombre": categoria.nombre} for categoria in lista_categorias]
    return jsonify(categorias)