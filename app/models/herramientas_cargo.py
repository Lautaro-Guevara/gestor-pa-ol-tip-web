from app import db

class HerramientasACargo(db.Model):
    __tablename__ = 'herramientas_a_cargo'
    
    id_herramientas_a_cargo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    legajo_personal = db.Column(db.Integer, db.ForeignKey('personal.legajo_personal'), nullable=False)
