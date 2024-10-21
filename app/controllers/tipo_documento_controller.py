from flask import jsonify
from app.models.tipo_documento import TipoDocumento
from app import db

def get_tipos_documento():
    tipos = TipoDocumento.query.all()
    return jsonify([{"id": t.id, "tipo": t.tipo, "nomenclatura": t.nomenclatura} for t in tipos])

def seed_tipos_documento():
    registros_iniciales = [
        ("CC", "Cédula de Ciudadanía"),
        ("CE", "Cédula de Extranjería"),
        ("TI", "Tarjeta de Identidad"),
        ("RC", "Registro Civil"),
        ("P", "Pasaporte"),
        ("LC", "Licencia de Conducción"),
        ("CIE", "Carné de Identidad de Grupos Étnicos"),
        ("CCi", "Certificado de Ciudadanía"),
        ("TR", "Tarjeta de Identidad para Residentes"),
        ("PD", "Pasaporte Diplomático"),
        ("PO", "Pasaporte Oficial"),
    ]

    for tipo, nomenclatura in registros_iniciales:
        nuevo_tipo_documento = TipoDocumento(tipo=tipo, nomenclatura=nomenclatura)
        db.session.add(nuevo_tipo_documento)

    db.session.commit()
    return {"message": "Registros iniciales de tipo_documento insertados"}
