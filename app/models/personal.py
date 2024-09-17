from app import db  # Importa la instancia de SQLAlchemy desde __init__.py
from .sector import Sector

class Personal(db.Model):
    __tablename__ = 'personal'
    
    legajo_personal = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    sector_id_sector = db.Column(db.Integer, db.ForeignKey('sector.id_sector'), nullable=True)

    # Relación con otras tablas
    herramientas_a_cargo = db.relationship('HerramientasACargo', backref='personal', lazy=True)
    herramientas_a_prestamo = db.relationship('HerramientasAPrestamo', backref='personal', lazy=True)
    elementos_numerados = db.relationship('ElementosNumerados', backref='personal', lazy=True)
    controles_diarios = db.relationship('ControlDiario', backref='personal', lazy=True)
