from flask import Blueprint, jsonify, request
from servicos.locacoes import LocacaoDatabase

locacao_blueprint = Blueprint("locacao", __name__)


@locacao_blueprint.route("/locacao", methods=["GET"])
def get_locacao():
  cpf =  request.args.get("cpf", "")
  linhas = LocacaoDatabase().get_locacao(cpf)
  
  return jsonify(linhas),200

@locacao_blueprint.route("/locacao", methods=["POST"])
def post_carros():
    json = request.get_json()
    cnh = request.get_json()
    valor_locacao = request.get_json()
    hora_locacao = request.get_json()
    data_retirada = request.get_json()
    data_devolucao_prevista = request.get_json()
    data_devolucao_efetiva = request.get_json()
    id_locacao = request.get_json()
    cpf = request.get_json()
    placa_veiculo_locacao = request.get_json()


    LocacaoDatabase().registra_locacao(cnh, valor_locacao, hora_locacao, data_retirada, data_devolucao_prevista, data_devolucao_efetiva, id_locacao, cpf, placa_veiculo_locacao)
    return jsonify("Cadastro de carro requisitado: "), 200
