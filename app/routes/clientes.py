from flask import Blueprint
from app.controllers.clientes_controller import crear_cliente, obtener_cliente_por_documento

clientes_bp = Blueprint('clientes', __name__)

@clientes_bp.route('/clientes', methods=['POST'])
def registrar_cliente():
    return crear_cliente()

@clientes_bp.route('/clientes', methods=['GET'])
def consultar_cliente():
    return obtener_cliente_por_documento()
