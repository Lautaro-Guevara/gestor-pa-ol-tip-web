from app import db

class Sector(db.Model):
    __tablename__ = 'sector'
    
    id_sector = db.Column(db.Integer, primary_key=True)
    nombre_sector = db.Column(db.String(45), nullable=False)
    area_id_area = db.Column(db.Integer, db.ForeignKey('area.id_area'), nullable=False)
    
    # Relación uno a muchos con Personal
    personal = db.relationship('Personal', backref='sector', lazy=True)
