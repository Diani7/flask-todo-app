from . import db

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contenido = db.Column(db.String(100), nullable=False)
    completada = db.Column(db.Boolean, default=False)
