from flask import Blueprint, jsonify, request
from servicos.multas_atraso_devolucao import Multas_Atraso_DevolucaoDataBase


multas_atraso_devolucao_blueprint = Blueprint("multa_atraso_devolucao", __name__)

@multas_atraso_devolucao_blueprint.route("/multas_atraso_devolucao", methods=["GET"])
def get_multas_atraso_devolucao():
    id_multa = request.args.get("id_multa")
    if id_multa:
        id_multa = int(id_multa)
    return jsonify(Multas_Atraso_DevolucaoDataBase().get_multas_atraso_devolucao(id_multa)), 200


@multas_atraso_devolucao_blueprint.route("/multas_atraso_devolucao", methods=["POST"])
def post_multas_atraso_devolucao():
        id_multa_atraso_devolucao = json.get("id_multa_atraso_devolucao")
        Multas_Atraso_DevolucaoDataBase().registra_multa_atraso_devolucao(id_multa_atraso_devolucao)
        return jsonify("Inserir Multa_Atraso_Devolucao")
