from app import db

class Elementos(db.Model):
    __tablename__ = 'elementos'
    
    id_elementos = db.Column(db.Integer, primary_key=True)
    id_categorias_inventario = db.Column(db.Integer, db.ForeignKey('categorias_inventario.id_categorias_inventario'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    
    # Relación con Control Diario y Stock
    controles_diarios = db.relationship('ControlDiario', backref='elemento', lazy=True)
    stock = db.relationship('Stock', backref='elemento', lazy=True)
