from app import db

class TipoCredito(db.Model):
    __tablename__ = 'tipo_credito'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<TipoCredito {self.tipo}>"
