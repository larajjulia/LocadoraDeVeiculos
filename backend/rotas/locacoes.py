from flask import Blueprint, jsonify, request
from servicos.locacoes import LocacaoDatabase
from decimal import Decimal

locacao_blueprint = Blueprint("locacao", __name__)


def converter(valor):
    if isinstance(valor, Decimal):
        return float(valor)
    if valor is None:
        return None
    if isinstance(valor, (int, float, str, bool)):
        return valor
    return str(valor)


@locacao_blueprint.route("/locacao", methods=["GET"])
def get_locacao():
  cpf =  request.args.get("cpf", "")
  carro = request.args.get("carro", "")
  linhas = LocacaoDatabase().get_locacao(cpf, carro)
  locacoes = [{k: converter(v) for k, v in linha.items()} for linha in linhas]
  
  return jsonify(locacoes),200