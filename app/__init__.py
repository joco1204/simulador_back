from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.models.tipo_credito import TipoCredito
    from app.models.marca_moto import MarcaMoto
    from app.models.linea_moto import LineaMoto
    from app.models.tipo_documento import TipoDocumento
    from app.models.clientes import Cliente
    from app.models.credito import Credito
    from app.models.periodo_pago import PeriodoPago
    from app.routes import tipo_credito_bp, marca_moto_bp, linea_moto_bp, tipo_documento_bp, clientes_bp, credito_bp, periodo_pago_bp
    
    app.register_blueprint(tipo_credito_bp)
    app.register_blueprint(marca_moto_bp)
    app.register_blueprint(linea_moto_bp)
    app.register_blueprint(tipo_documento_bp)
    app.register_blueprint(clientes_bp)
    app.register_blueprint(credito_bp)
    app.register_blueprint(periodo_pago_bp)

    return app