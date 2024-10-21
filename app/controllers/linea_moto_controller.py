from flask import jsonify, request
from app import db
from app.models.linea_moto import LineaMoto

def get_lineas_moto(id_marca):
    lineas = LineaMoto.query.filter_by(id_marca_moto=id_marca).all()
    base_url = request.host_url  # Obtener la URL base
    return jsonify([{
        'id': l.id,
        'linea': l.linea,
        'precio': str(l.precio),
        'url_imagen': f"{base_url}{l.url_imagen}"
    } for l in lineas])

def seed_lineas_moto():
    registros_iniciales = [
        (1, 'GIXXER 150 FI', 11300000, '/imagenes/suzuki_gixxer_150_fi.jpg'),
        (1, 'GN 125', 8100000, '/imagenes/suzuki_gn_125.jpg'),
        (2, 'CR4 125', 8500000, '/imagenes/akt_cr4_125.jpg'),
        (2, 'NKD 125', 7500000, '/imagenes/akt_nkd_125.jpg'),
        (3, 'APACHE RTR 160 2V', 12900000, '/imagenes/auteco_apache_rtr_160_2v.jpg'),
        (3, 'TVS RAIDER 125', 10200000, '/imagenes/auteco_apache_tvs_raider_125.jpg')
    ]

    for id_marca, linea, precio, url_imagen in registros_iniciales:
        nueva_linea = LineaMoto(id_marca_moto=id_marca, linea=linea, precio=precio, url_imagen=url_imagen)
        db.session.add(nueva_linea)
    
    db.session.commit()
    return {"message": "Registros iniciales insertados"}
