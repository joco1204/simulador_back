from app import db

class LineaMoto(db.Model):
    __tablename__ = 'linea_moto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_marca_moto = db.Column(db.Integer, db.ForeignKey('marca_moto.id'), nullable=False)
    linea = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    url_imagen = db.Column(db.Text, nullable=False)

    marca_moto = db.relationship('MarcaMoto', backref='lineas')

    def __repr__(self):
        return f"<LineaMoto {self.linea}>"
