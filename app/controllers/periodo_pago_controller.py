from flask import jsonify, request
from app import db
from app.models.periodo_pago import PeriodoPago

def get_all_periodos():
    periodos = PeriodoPago.query.all()
    periodos_list = [
        {'id': periodo.id, 'periodo': periodo.periodo, 'dias': periodo.dias}
        for periodo in periodos
    ]
    return jsonify(periodos_list), 200

def get_dias_by_id(id):
    periodo = PeriodoPago.query.get(id)
    if periodo:
        return jsonify({'dias': periodo.dias}), 200
    else:
        return jsonify({'message': 'Periodo no encontrado'}), 200

def seed_periodos():
    periodos_iniciales = [
        {'periodo': 'Semanal', 'dias': 8},
        {'periodo': 'Quincenal', 'dias': 15},
        {'periodo': 'Mensual', 'dias': 30}
    ]
    
    for data in periodos_iniciales:
        periodo = PeriodoPago.query.filter_by(periodo=data['periodo']).first()
        if not periodo:
            nuevo_periodo = PeriodoPago(periodo=data['periodo'], dias=data['dias'])
            db.session.add(nuevo_periodo)
    
    db.session.commit()
    return jsonify({'message': 'Registros iniciales insertados con éxito'}), 201
