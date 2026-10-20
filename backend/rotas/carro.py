from flask import Blueprint
from flask import jsonify, request

from servicos.carro import CarrosDoDatabase

carros_blueprint = Blueprint("carro", __name__)

@carros_blueprint.route("/carros", methods=["GET"])
def get_carros():
    categoria = request.args.get("categoria", "")
    cliente = request.args.get("cliente", "")
    locacao = request.args.get("locacao", "")
    return jsonify(CarrosDoDatabase().get_carros(categoria, cliente, locacao)), 200

@carros_blueprint.route("/carros", methods=["POST"])
def post_carros():
    json = request.get_json()
    categoria = request.get_json()
    placa_veiculo = request.get_json()
    modelo = request.get_json()
    quilometragem = request.get_json()
    estado = request.get_json()
    valor_seguro = request.get_json()
    valor_diaria = request.get_json()
    CarrosDoDatabase().registra_carro(categoria, placa_veiculo, modelo, quilometragem, estado, valor_seguro, valor_diaria)
    return jsonify("Cadastro de carro requisitado: "), 200

