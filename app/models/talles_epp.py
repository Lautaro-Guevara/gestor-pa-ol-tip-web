from app import db

class TallesEpp(db.Model):
    __tablename__ = 'talles_epp'
    
    id_talles_epp = db.Column(db.Integer, primary_key=True)
    talle = db.Column(db.String(45), nullable=False)
    genero = db.Column(db.Enum("Hombre", "Mujer", "Unisex"), nullable=False)
    tipo_vestimenta_epp_id_tipo_vestimenta_epp = db.Column(db.Integer, db.ForeignKey('tipo_vestimenta_epp.id_tipo_vestimenta_epp'), nullable=False)
