from flask import Blueprint
from app.controllers.credito_controller import crear_credito, obtener_creditos_por_cliente

credito_bp = Blueprint('credito', __name__)

@credito_bp.route('/credito', methods=['POST'])
def registrar_credito():
    return crear_credito()

@credito_bp.route('/credito/<int:id_cliente>', methods=['GET'])
def consultar_creditos(id_cliente):
    return obtener_creditos_por_cliente(id_cliente)
