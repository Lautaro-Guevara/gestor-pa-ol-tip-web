from app import db

class TipoVestimentaEpp(db.Model):
    __tablename__ = 'tipo_vestimenta_epp'
    
    id_tipo_vestimenta_epp = db.Column(db.Integer, primary_key=True, autoincrement=True)
    descripcion = db.Column(db.String(45), nullable=False, unique=True)
    
    # Relación con TallesEpp
    talles = db.relationship('TallesEpp', backref='tipo_vestimenta', lazy=True)
