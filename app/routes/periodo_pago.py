from flask import Blueprint
from app.controllers.periodo_pago_controller import get_all_periodos, get_dias_by_id, seed_periodos

periodo_pago_bp = Blueprint('periodo_pago', __name__)

# GET: Listar todos los periodos
@periodo_pago_bp.route('/periodo', methods=['GET'])
def listar_periodos():
    return get_all_periodos()

# GET: Obtener los días según el ID del periodo
@periodo_pago_bp.route('/periodo/<int:id>', methods=['GET'])
def obtener_dias_por_id(id):
    return get_dias_by_id(id)

# POST: Insertar registros iniciales (seed)
@periodo_pago_bp.route('/periodo/seed', methods=['POST'])
def insertar_seed_periodos():
    return seed_periodos()