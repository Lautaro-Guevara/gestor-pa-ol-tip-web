from app import db

class HerramientasACargo(db.Model):
    __tablename__ = 'herramientas_a_cargo'

    id_herramientas_a_cargo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    legajo_personal = db.Column(db.Integer, db.ForeignKey('personal.legajo_personal'), nullable=False)
    fecha_entrega = db.Column(db.Date)
    herramienta = db.Column(db.String(100))
    id_herramienta = db.Column(db.String(10))
    procedencia = db.Column(db.Integer, db.ForeignKey('personal.legajo_personal'), nullable=False)
    observacion = db. Column(db.String(100))


class DevolucionHerramientasACargo(db.Model):
    __tablename__ = "devolucion_herramientas_a_cargo"

    id_registro_devolucion = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_registro_entrega = db.Column(db.Integer, db.ForeignKey("herramientas_a_cargo.id_herramientas_a_cargo"), nullable=False)
    fecha_devolucion = db.Column(db.Date)
    estado = db.Column(db.Enum("Sano", "Roto", "Perdido"))
    observacion = db. Column(db.String(100))
