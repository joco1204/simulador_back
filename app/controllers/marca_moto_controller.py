from flask import jsonify
from app.models.marca_moto import MarcaMoto
from app import db

def get_marcas_moto():
    marcas = MarcaMoto.query.all()
    return jsonify([{"id": m.id, "marca": m.marca} for m in marcas])

def seed_marcas_moto():
    registros_iniciales = ['Suzuki', 'AKT', 'Auteco']

    for marca in registros_iniciales:
        nueva_marca = MarcaMoto(marca=marca)
        db.session.add(nueva_marca)

    db.session.commit()
    return {"message": "Registros iniciales de marca_moto insertados"}
