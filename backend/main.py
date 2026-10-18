### API

from flask import Flask, jsonify
from flask_cors import CORS
from rotas.clientes import cliente_blueprint

# temos um servidor, em que vamos cadastrar algumas rotas
# Rotas: servem para buscar informações nessa API
app = Flask(__name__)

CORS(app, origins="*")

@app.route("/", methods=["GET"])
def get_std():
    return jsonify("It's alive"), 200 # status code => 200: buscando alguam informação

# cadastrar a rota de cliente
app.register_blueprint(cliente_blueprint)

app.run("0.0.0.0", port=8000, debug=False)