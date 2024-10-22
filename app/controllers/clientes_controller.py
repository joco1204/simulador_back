from flask import jsonify, request
from app.models.clientes import Cliente
from app import db

def crear_cliente():
    data = request.get_json()
    if not data:
        return jsonify({"message": "No se recibieron datos"}), 200

    try:
        nuevo_cliente = Cliente(
            id_tipo_documento=data['id_tipo_documento'],
            numero_documento=data['numero_documento'],
            nombres=data['nombres'],
            apellidos=data['apellidos'],
            celular=data['celular'],
            direccion=data.get('direccion', ''),
            barrio=data.get('barrio', ''),
            ciudad=data.get('ciudad', ''),
            departamento=data.get('departamento', ''),
            nombre_referencia_1=data.get('nombre_referencia_1', ''),
            celular_referencia_1=data.get('celular_referencia_1', ''),
            nombre_referencia_2=data.get('nombre_referencia_2', ''),
            celular_referencia_2=data.get('celular_referencia_2', ''),
        )

        db.session.add(nuevo_cliente)
        db.session.commit()
        return jsonify({"message": "Cliente creado", "id": nuevo_cliente.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500

def obtener_cliente_por_documento():
    tipo_documento = request.args.get('tipo_documento')
    numero_documento = request.args.get('numero_documento')

    cliente = Cliente.query.filter_by(numero_documento=numero_documento, id_tipo_documento=tipo_documento).first()
    
    if cliente:
        return jsonify({
            "id": cliente.id,
            "tipo_documento": tipo_documento,
            "numero_documento": cliente.numero_documento,
            "nombres": cliente.nombres,
            "apellidos": cliente.apellidos,
            "celular": cliente.celular,
            "direccion": cliente.direccion,
            "barrio": cliente.barrio,
            "ciudad": cliente.ciudad,
            "departamento": cliente.departamento,
            "nombre_referencia_1": cliente.nombre_referencia_1,
            "celular_referencia_1": cliente.celular_referencia_1,
            "nombre_referencia_2": cliente.nombre_referencia_2,
            "celular_referencia_2": cliente.celular_referencia_2
        }), 200
    else:
        return jsonify({"message": "No se encontró registro"}), 200
