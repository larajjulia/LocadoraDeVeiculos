from flask import blueprints


multa_blueprint = Blueprint ("multa", __name__)

@multas.blueprint.route("/multa", methods=["GET"])
def get_multa():
    return jsonify(), 200