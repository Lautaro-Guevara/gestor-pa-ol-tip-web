from app import db

class Matafuegos(db.Model):
    __tablename__ = 'matafuegos'
    
    id_matafuego = db.Column(db.Integer, primary_key=True)
    fecha_ingreso = db.Column(db.Date, nullable=True)
    capacidad_matafuego = db.Column(db.Enum('1 kg', '2.5 kg', '5 kg', '10 kg'), nullable=False)
    fecha_vencimiento = db.Column(db.Date, nullable=False)
    fecha_vencimiento_prueba_hidraulica = db.Column(db.Date, nullable=False)
    ubicacion_actual_matafuego = db.Column(db.String(100), nullable=True)
    ubicacion_anterior_matafuego = db.Column(db.String(100), nullable=True)
    fecha_ultimo_movimiento = db.Column(db.Date, nullable=True)
    despresurizado = db.Column(db.String(45), nullable=True)
    matafuegoscol = db.Column(db.Boolean, nullable=True)
    
    # Relación con Control Diario
    controles_diarios = db.relationship('ControlDiario', backref='matafuego', lazy=True)
