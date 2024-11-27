from app import db

class CategoriasInventario(db.Model):
    __tablename__ = 'categorias_inventario'
    
    id_categorias_inventario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    id_padre = db.Column(db.Integer, db.ForeignKey('categorias_inventario.id_categorias_inventario'), nullable=True)
    
    # Relación de jerarquía en la misma tabla (categorías padre-hijo)
    subcategorias = db.relationship(
        'CategoriasInventario', 
        backref=db.backref('padre', remote_side=[id_categorias_inventario]), 
        lazy=True
    )

    # Relación con Elementos
    elementos = db.relationship('Elementos', backref='categoria', lazy=True)
