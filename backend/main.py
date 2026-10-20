"Camada de Gerenciamento do Database"

from flask import Flask, jsonify
from rotas.carro import carros_blueprint

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_carro():
    return jsonify("It's alive"), 200

app.register_blueprint(carros_blueprint)

app.run("0.0.0.0", port=8000, debug=False)