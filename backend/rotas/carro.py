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