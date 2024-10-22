from flask import request, jsonify
from app import db
from app.models.credito import Credito
from datetime import datetime

def crear_credito():
    try:
        data = request.get_json()
        
        nuevo_credito = Credito(
            id_cliente=data['id_cliente'],
            id_tipo_credito=data['id_tipo_credito'],
            id_linea_moto=data.get('id_linea_moto'),
            id_periodo_pago=data['id_periodo_pago'],
            valor_solicitud=data['valor_solicitud'],
            valor_interes=data['valor_interes'],
            valor_cuota=data['valor_cuota'],
            valor_total=data['valor_total'],
            fecha_solicitud=datetime.strptime(data['fecha_solicitud'], '%Y-%m-%d %H:%M:%S'),
            fecha_inicio_credito=datetime.strptime(data['fecha_inicio_credito'], '%Y-%m-%d'),
            fecha_fin=datetime.strptime(data['fecha_fin'], '%Y-%m-%d'),
            credito=data['credito'],
            estado=data['estado']
        )

        db.session.add(nuevo_credito)
        db.session.commit()

        return jsonify({'message': 'Crédito creado con éxito'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

def obtener_creditos_por_cliente():
    try:
        id_cliente = request.args.get('id_cliente')
        creditos = Credito.query.filter_by(id_cliente=id_cliente).all()

        if not creditos:
            return jsonify({'message': 'No se encontraron créditos para este cliente'}), 404

        result = []
        for credito in creditos:
            result.append({
                'id': credito.id,
                'valor_solicitud': str(credito.valor_solicitud),
                'valor_interes': str(credito.valor_interes),
                'valor_cuota': str(credito.valor_cuota),
                'id_linea_moto': str(credito.id_linea_moto),
                'valor_total': str(credito.valor_total),
                'fecha_solicitud': credito.fecha_solicitud.strftime('%Y-%m-%d %H:%M:%S'),
                'fecha_inicio_credito': credito.fecha_inicio_credito.strftime('%Y-%m-%d'),
                'fecha_fin': credito.fecha_fin.strftime('%Y-%m-%d'),
                'credito': str(credito.credito),
                'estado': credito.estado
            })

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
