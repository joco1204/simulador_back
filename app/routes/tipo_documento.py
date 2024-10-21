from flask import Blueprint
from app.controllers.tipo_documento_controller import get_tipos_documento, seed_tipos_documento

tipo_documento_bp = Blueprint('tipo_documento', __name__)

@tipo_documento_bp.route('/tipo_documento', methods=['GET'])
def listar_tipos_documento():
    return get_tipos_documento()

@tipo_documento_bp.route('/tipo_documento/seed', methods=['POST'])
def sembrar_tipos_documento():
    return seed_tipos_documento()
