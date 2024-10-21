from app import db

class Credito(db.Model):
    __tablename__ = 'credito'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    id_tipo_credito = db.Column(db.Integer, db.ForeignKey('tipo_credito.id'), nullable=False)
    id_linea_moto = db.Column(db.Integer, nullable=True)  # No es llave foránea y permite nulo
    valor_solicitud = db.Column(db.Numeric(10, 2), nullable=False)
    valor_interes = db.Column(db.Numeric(10, 2), nullable=False)
    valor_cuota = db.Column(db.Numeric(10, 2), nullable=False)
    valor_total = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<Credito {self.id}>"
