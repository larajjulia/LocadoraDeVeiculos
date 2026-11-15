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
    categoria = json["categoria"]
    placa_veiculo = json["placa_veiculo"]
    modelo = json["modelo"]
    quilometragem = json["quilometragem"]
    estado = json["estado"]
    valor_seguro = json["valor_seguro"]
    valor_diaria = json["valor_diaria"]
    CarrosDoDatabase().registra_carro(categoria, placa_veiculo, modelo, quilometragem, estado, valor_seguro, valor_diaria)
    return jsonify("Cadastro de carro requisitado: "), 200

