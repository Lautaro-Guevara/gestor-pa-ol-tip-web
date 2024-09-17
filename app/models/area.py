from app import db

class Area(db.Model):
    __tablename__ = 'area'
    
    id_area = db.Column(db.Integer, primary_key=True)
    nombre_area = db.Column(db.String(45), nullable=False)
    
    # Relación con la tabla Sector
    sectores = db.relationship('Sector', backref='area', lazy=True)

    def __repr__(self):
        return f"<Area {self.nombre_area}>"
