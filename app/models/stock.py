from app import db

class Stock(db.Model):
    __tablename__ = 'stock'
    
    id_stock = db.Column(db.Integer, primary_key=True)
    id_elemento = db.Column(db.Integer, db.ForeignKey('elementos.id_elementos'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    imputacion = db.Column(db.String(45), nullable=True)
