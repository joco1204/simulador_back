from app import db
from datetime import datetime

class Credito(db.Model):
    __tablename__ = 'credito'

    id = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    id_tipo_credito = db.Column(db.Integer, db.ForeignKey('tipo_credito.id'), nullable=False)
    id_linea_moto = db.Column(db.Integer, nullable=True)
    id_periodo_pago = db.Column(db.Integer, db.ForeignKey('periodo_pago.id'), nullable=False)
    valor_solicitud = db.Column(db.Numeric(10, 0), nullable=False)
    numero_cuotas = db.Column(db.Numeric(10, 0), nullable=False)
    valor_interes = db.Column(db.Numeric(10, 0), nullable=False)
    valor_cuota_mensual = db.Column(db.Numeric(10, 0), nullable=False)
    valor_cuota_periodo = db.Column(db.Numeric(10, 0), nullable=False)
    valor_total = db.Column(db.Numeric(10, 0), nullable=False)
    fecha_solicitud = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_inicio_credito = db.Column(db.DateTime, nullable=False)
    fecha_fin_credito = db.Column(db.DateTime, nullable=False)
    estado = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Credito {self.id}>'

