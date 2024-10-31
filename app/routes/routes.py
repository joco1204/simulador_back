from flask import Blueprint, send_from_directory, abort

imagenes_pb = Blueprint('imagenes', __name__)

@imagenes_pb.route('api/imagenes/<filename>', methods=['GET'])
def obtener_imagen(filename):
    try:
        return send_from_directory('static/imagenes', filename)
    except FileNotFoundError:
        abort(404) 
