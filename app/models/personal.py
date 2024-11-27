from app import db  # Importa la instancia de SQLAlchemy desde __init__.py
from .sector import Sector

class Personal(db.Model):
    __tablename__ = 'personal'
    
    legajo_personal = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellido = db.Column(db.String(45), nullable=False)
    sector_id_sector = db.Column(db.Integer, db.ForeignKey('sector.id_sector'), nullable=True)

    # Relación con herramientas_a_cargo utilizando legajo_personal como clave foránea
    herramientas_a_cargo = db.relationship(
        'HerramientasACargo',
        backref='personal',  # Relación estándar con legajo_personal
        lazy=True,
        foreign_keys='HerramientasACargo.legajo_personal'
    )

    # Relación con herramientas_a_cargo utilizando procedencia como clave foránea
    herramientas_a_cargo_procedencia = db.relationship(
        'HerramientasACargo',
        backref='procedente',  # Relación para la columna procedencia
        lazy=True,
        foreign_keys='HerramientasACargo.procedencia'
    )

    # Relación con herramientas a préstamo
    herramientas_a_prestamo = db.relationship(
        'HerramientasAPrestamo',
        backref='personal',
        lazy=True
    )

    # Relación con elementos numerados
    elementos_numerados = db.relationship(
        'ElementosNumerados',
        backref='personal',
        lazy=True
    )

    # Relación con controles diarios
    controles_diarios = db.relationship(
        'ControlDiario',
        backref='personal',
        lazy=True
    )

