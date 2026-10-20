from flask import Blueprint
from flask import jsonify

from servicos.database.carro import CarrosDoDatabase

carros_blueprint = Blueprint("carro", __name__)

@carros_blueprint.route("/carros", methods=["GET"])
def get_carros():
    return jsonify(CarrosDoDatabase().get_carros()), 200