from app import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_tipo_documento = db.Column(db.Integer, db.ForeignKey('tipo_documento.id'), nullable=False)
    numero_documento = db.Column(db.String(12), nullable=False)
    nombres = db.Column(db.String(255), nullable=False)
    apellidos = db.Column(db.String(255), nullable=False)
    celular = db.Column(db.String(10), nullable=False)
    direccion = db.Column(db.String(100))
    barrio = db.Column(db.String(100))
    ciudad = db.Column(db.String(50))
    departamento = db.Column(db.String(50))
    nombre_referencia_1 = db.Column(db.String(100))
    celular_referencia_1 = db.Column(db.String(10))
    nombre_referencia_2 = db.Column(db.String(100))
    celular_referencia_2 = db.Column(db.String(10))

    def __repr__(self):
        return f"<Cliente {self.nombres} {self.apellidos}>"