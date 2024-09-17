from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_mysqldb import MySQL
from flask_migrate import Migrate



db = SQLAlchemy()
migrate = Migrate()
from .models import *
def create_app():

    # Configuraciones Basicas
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'una_clave_secreta_aleatoria'  # Necesaria para mantener la seguridad en las sesiones
    
    # Configuracion Base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:tipsadb@localhost/pañol_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)
    migrate.init_app(app, db)
    

    # Blueprints
    from .routes import index_bp, lista_personal_bp, entregas_diarias_bp, matafuegos_bp, stock_bp
    app.register_blueprint(index_bp)
    app.register_blueprint(lista_personal_bp)
    app.register_blueprint(entregas_diarias_bp)
    app.register_blueprint(matafuegos_bp)
    app.register_blueprint(stock_bp)

    # Manejadores de errores
    @app.errorhandler(404)
    def not_found_error(error):
        return "Página no encontrada", 404

    return app
