from app import db

class CategoriasInventario(db.Model):
    __tablename__ = 'categorias_inventario'
    
    id_categorias_inventario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    
    # Relación con Elementos
    elementos = db.relationship('Elementos', backref='categoria', lazy=True)
