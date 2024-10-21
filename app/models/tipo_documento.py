from app import db

class TipoDocumento(db.Model):
    __tablename__ = 'tipo_documento'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(100), nullable=False)
    nomenclatura = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<TipoDocumento {self.tipo}>"
