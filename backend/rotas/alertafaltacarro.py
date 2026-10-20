from flask import Blueprint
from flask import jsonify

from servicos.alertafaltacarro import AlertaFaltaCarroDatabase

alertafaltacarro_blueprint = Blueprint("alertafaltacarro", __name__)

@alertafaltacarro_blueprint.route("/carros", methods=["GET"])
def get_carros():
    return jsonify(AlertaFaltaCarroDatabase().get_alertafaltacarros()), 200