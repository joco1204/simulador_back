from app import db

class PeriodoPago(db.Model):
    __tablename__ = 'periodo_pago'

    id = db.Column(db.Integer, primary_key=True)
    periodo = db.Column(db.String(50), nullable=False)
    dias = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<PeriodoPago(id={self.id}, periodo='{self.periodo}', dias={self.dias})>"
