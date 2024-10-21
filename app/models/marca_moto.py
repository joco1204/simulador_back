from app import db

class MarcaMoto(db.Model):
    __tablename__ = 'marca_moto'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    marca = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<MarcaMoto {self.marca}>"
