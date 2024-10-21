from flask import jsonify, request
from app.models.credito import Credito
from app import db

def crear_credito():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No se recibieron datos"}), 400

    try:
        nuevo_credito = Credito(
            id_cliente=data['id_cliente'],
            id_tipo_credito=data['id_tipo_credito'],
            id_linea_moto=data.get('id_linea_moto'), 
            valor_solicitud=data['valor_solicitud'],
            valor_interes=data['valor_interes'],
            valor_cuota=data['valor_cuota'],
            valor_total=data['valor_total']
        )

        db.session.add(nuevo_credito)
        db.session.commit()
        return jsonify({"message": "Crédito creado", "id": nuevo_credito.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

def obtener_creditos_por_cliente(id_cliente):
    creditos = Credito.query.filter_by(id_cliente=id_cliente).all()
    
    if not creditos:
        return jsonify({"message": "No se encontraron créditos activos para el cliente"}), 404
    
    resultado = []
    for credito in creditos:
        resultado.append({
            "id": credito.id,
            "id_cliente": credito.id_cliente,
            "id_tipo_credito": credito.id_tipo_credito,
            "id_linea_moto": credito.id_linea_moto,
            "valor_solicitud": str(credito.valor_solicitud),
            "valor_interes": str(credito.valor_interes),
            "valor_cuota": str(credito.valor_cuota),
            "valor_total": str(credito.valor_total)
        })

    return jsonify(resultado), 200
