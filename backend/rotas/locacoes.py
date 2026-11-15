from flask import Blueprint, jsonify, request
from servicos.locacoes import LocacaoDatabase

locacao_blueprint = Blueprint("locacao", __name__)


@locacao_blueprint.route("/locacao", methods=["GET"])
def get_locacao():
  cpf =  request.args.get("cpf", "")
  linhas = LocacaoDatabase().get_locacao(cpf)
  
  return jsonify(linhas),200

@locacao_blueprint.route("/locacao_registrar", methods=["POST"])
def post_carros():
    json = request.get_json()
    cnh = json.get("cnh")
    valor_locacao = json.get("valor_locacao")
    valor_total = json.get("valor_total")
    hora_locacao = json.get("hora_locacao")
    data_retirada = json.get("data_retirada")
    data_devolucao_prevista = json.get("data_devolucao_prevista")
    data_devolucao_efetiva = json.get("data_devolucao_efetiva")
    id_locacao = json.get("id_locacao")
    cpf = json.get("cpf")
    placa_veiculo = json.get("placa_veiculo")


    LocacaoDatabase().registra_locacao(cnh, valor_locacao, valor_total, hora_locacao, data_retirada, data_devolucao_prevista, data_devolucao_efetiva, id_locacao, cpf, placa_veiculo)
    return jsonify("Nova locação registrada!"), 200
