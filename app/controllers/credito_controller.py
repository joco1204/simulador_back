from flask import request, jsonify
from app import db
from app.models.credito import Credito
from datetime import datetime

def crear_credito():
    try:
        data = request.get_json()
        
        id_linea_moto = data.get('id_linea_moto')
        if id_linea_moto == 'undefined' or id_linea_moto is None:
            id_linea_moto = None 

        nuevo_credito = Credito(
            id_cliente=data['id_cliente'],
            id_tipo_credito=data['id_tipo_credito'],
            id_linea_moto=id_linea_moto,
            id_periodo_pago=data['id_periodo_pago'],
            valor_solicitud=data['valor_solicitud'],
            numero_cuotas=data['numero_cuotas'],
            valor_interes=data['valor_interes'],
            valor_cuota_mensual=data['valor_cuota_mensual'],
            valor_cuota_periodo=data['valor_cuota_periodo'],
            valor_total=data['valor_total'],
            fecha_solicitud=datetime.strptime(data['fecha_solicitud'], '%Y-%m-%d'),
            fecha_inicio_credito=datetime.strptime(data['fecha_inicio_credito'], '%Y-%m-%d'),
            fecha_fin_credito=datetime.strptime(data['fecha_fin_credito'], '%Y-%m-%d'),
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
            return jsonify({'message': 'No se encontraron créditos para este cliente'}), 200

        result = []
        for credito in creditos:
            result.append({
                'id': credito.id,
                'id_cliente': str(credito.id_cliente),
                'id_tipo_credito': str(credito.id_tipo_credito),
                'id_periodo_pago': str(credito.id_periodo_pago),
                'valor_solicitud': str(credito.valor_solicitud),
                'numero_cuotas': str(credito.numero_cuotas),
                'valor_interes': str(credito.valor_interes),
                'valor_cuota_mensual': str(credito.valor_cuota_mensual),
                'valor_cuota_periodo': str(credito.valor_cuota_periodo),
                'id_linea_moto': str(credito.id_linea_moto),
                'valor_total': str(credito.valor_total),
                'fecha_solicitud': credito.fecha_solicitud.strftime('%Y-%m-%d'),
                'fecha_inicio_credito': credito.fecha_inicio_credito.strftime('%Y-%m-%d'),
                'fecha_fin_credito': credito.fecha_fin.strftime('%Y-%m-%d'),
                'estado': credito.estado
            })

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
