from app import db

class MatafuegosRecarga(db.Model):
    __tablename__ = 'matafuegos_recarga'
    
    id_matafuegos_recarga = db.Column(db.Integer, primary_key=True)
    fecha_enviado = db.Column(db.Date, nullable=False)
    fecha_recibido = db.Column(db.Date, nullable=False)
    activo = db.Column(db.Boolean, nullable=False)
