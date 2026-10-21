from flask import Blueprint, jsonify, request
from servicos.locacoes import LocacaoDatabase
from decimal import Decimal

locacao_blueprint = Blueprint("locacao", __name__)


# def converter(valor):
#     if isinstance(valor, Decimal):
#         return float(valor)
#     if valor is None:
#         return None
#     if isinstance(valor, (int, float, str, bool)):
#         return valor
#     return str(valor)


@locacao_blueprint.route("/locacao", methods=["GET"])
def get_locacao():
  cpf =  request.args.get("cpf", "")
  linhas = LocacaoDatabase().get_locacao(cpf)
  
  return jsonify(linhas),200