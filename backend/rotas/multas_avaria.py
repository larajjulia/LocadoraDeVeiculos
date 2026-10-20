from flask import Blueprint, jsonify, request
from backend.servicos.multas_avaria import Multas_AvariaDataBase


multas_avaria_blueprint = Blueprint("multa_avaria", __name__)

@multas_avaria_blueprint.route("/multas_avaria", methods=["GET"])
def get_multas_avaria():
    id_multa = request.args.get("id_multa")
    if id_multa:
        id_multa = int(id_multa)
    return jsonify(Multas_AvariaDataBase().get_multas_avaria(id_multa)), 200

@multas_avaria_blueprint.route("/multas_avaria", methods=["POST"])
def post_multas_avaria():
        id_multa_avaria = json.get("id_multa_avaria")
        grau = json.get("grau")
        Multas_AvariaDataBase().registra_multa_avaria(id_multa_avaria, grau)
        return jsonify("Inserir Multa_Avaria")

