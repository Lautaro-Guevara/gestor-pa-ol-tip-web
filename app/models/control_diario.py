from app import db
from .personal import Personal  # Importar la referencia cruzada
from .elementos import Elementos
from .matafuegos import Matafuegos

class ControlDiario(db.Model):
    __tablename__ = 'control_diario'
    
    id_control_diario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_elemento = db.Column(db.Integer, db.ForeignKey('elementos.id_elementos'), nullable=True)
    legajo_personal = db.Column(db.Integer, db.ForeignKey('personal.legajo_personal'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    comentarios = db.Column(db.String(45), nullable=True)
    id_matafuego = db.Column(db.Integer, db.ForeignKey('matafuegos.id_matafuego'), nullable=True)
    accion = db.Column(db.Enum('Retiro', 'Prestamo', 'Dejo', 'Devolvio', 'Intercambio', 'A Cargo'), nullable=False)
