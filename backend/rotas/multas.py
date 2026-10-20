from flask import Blueprint, jsonify, request
from servicos.multas import MultasDataBase


multas_blueprint = Blueprint("multa", __name__)

@multas_blueprint.route("/multas", methods=["GET"])
def get_multas():
    id_locacao = request.args.get("id_locacao")
    if id_locacao:
        id_locacao = int(id_locacao)
    return jsonify(MultasDataBase().get_multas(id_locacao)), 200

@multas_blueprint.route("/multas", methods=["POST"])
def post_multas():
    json = request.get_json()
    valor_multa = json.get("valor")
    status = json.get("status")
    id_multa = json.get("id_multa")
    MultasDataBase().registra_multa(valor_multa, status, id_multa)
    return jsonify("Inserir Multa")
