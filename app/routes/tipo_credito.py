from flask import Blueprint
from app.controllers.tipo_credito_controller import get_tipos_credito, seed_tipos_credito

tipo_credito_bp = Blueprint('tipo_credito', __name__)

@tipo_credito_bp.route('/tipo_credito', methods=['GET'])
def listar_tipos_credito():
    return get_tipos_credito()

@tipo_credito_bp.route('/tipo_credito/seed', methods=['POST'])
def sembrar_tipos_credito():
    return seed_tipos_credito()
