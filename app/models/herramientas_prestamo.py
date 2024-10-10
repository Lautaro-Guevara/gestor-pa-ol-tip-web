from app import db

class HerramientasAPrestamo(db.Model):
    __tablename__ = 'herramientas_a_prestamo'
    
    id_herramientas_a_prestamo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    legajo_personal = db.Column(db.Integer, db.ForeignKey('personal.legajo_personal'), nullable=False)
    fecha = db.Column(db.Date, nullable=True)
    herramienta = db.Column(db.String(45), nullable=True)
    observaciones = db.Column(db.String(45), nullable=True)
    fecha_devolucion = db.Column(db.Date, nullable=True)
