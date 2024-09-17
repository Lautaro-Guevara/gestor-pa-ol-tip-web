from app import db

class ElementosNumerados(db.Model):
    __tablename__ = 'elementos_numerados'
    
    id_numeracion_elementos = db.Column(db.Integer, primary_key=True)
    legajo_personal = db.Column(db.Integer, db.ForeignKey('personal.legajo_personal'), nullable=False)
    fecha_recepcion = db.Column(db.Date, nullable=True)
    categoria = db.Column(db.String(45), nullable=False)
    nombre_elemento = db.Column(db.String(45), nullable=False)
    marca_elemento = db.Column(db.String(45), nullable=False)
    modelo_elemento = db.Column(db.String(45), nullable=True)
