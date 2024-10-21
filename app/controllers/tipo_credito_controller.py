from flask import jsonify
from app.models.tipo_credito import TipoCredito
from app import db

def get_tipos_credito():
    tipos = TipoCredito.query.all()
    return jsonify([{"id": t.id, "tipo": t.tipo} for t in tipos])

def seed_tipos_credito():
    registros_iniciales = ['Microcrédito', 'Motocicleta', 'eBike']
    
    for tipo in registros_iniciales:
        nuevo_tipo = TipoCredito(tipo=tipo)
        db.session.add(nuevo_tipo)

    db.session.commit()
    return {"message": "Registros iniciales de tipo_credito insertados"}
