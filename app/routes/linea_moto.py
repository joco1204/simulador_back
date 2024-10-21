from flask import Blueprint
from app.controllers.linea_moto_controller import get_lineas_moto, seed_lineas_moto

linea_moto_bp = Blueprint('linea_moto', __name__)

@linea_moto_bp.route('/linea_moto/<int:id_marca>', methods=['GET'])
def listar_lineas_moto(id_marca):
    return get_lineas_moto(id_marca)

@linea_moto_bp.route('/linea_moto/seed', methods=['POST'])
def sembrar_lineas_moto():
    return seed_lineas_moto()
