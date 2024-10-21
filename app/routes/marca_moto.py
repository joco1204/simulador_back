from flask import Blueprint
from app.controllers.marca_moto_controller import get_marcas_moto, seed_marcas_moto

marca_moto_bp = Blueprint('marca_moto', __name__)

@marca_moto_bp.route('/marca_moto', methods=['GET'])
def listar_marcas_moto():
    return get_marcas_moto()

@marca_moto_bp.route('/marca_moto/seed', methods=['POST'])
def sembrar_marcas_moto():
    return seed_marcas_moto()
