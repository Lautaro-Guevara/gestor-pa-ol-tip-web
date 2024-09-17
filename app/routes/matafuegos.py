from flask import Blueprint, render_template, jsonify

matafuegos_bp = Blueprint("matafuegos", __name__)

@matafuegos_bp.route('/matafuegos.html')
def matafuegos():
    return render_template('matafuegos.html')

