### API

from flask import Flask, jsonify
from flask_cors import CORS
from rotas.clientes import cliente_blueprint
from rotas.carro import carros_blueprint
from rotas.alertafaltacarro import alertafaltacarro_blueprint
from rotas.multas import multas_blueprint
from rotas.multas_avaria import multas_avaria_blueprint
from rotas.multas_atraso_devolucao import multas_atraso_devolucao_blueprint
from __future__ import annotations

# temos um servidor, em que vamos cadastrar algumas rotas
# Rotas: servem para buscar informações nessa API
app = Flask(__name__)

CORS(app, origins="*")

@app.route("/", methods=["GET"])
def get_std():
    return jsonify("It's alive"), 200 # status code => 200: buscando alguam informação

# cadastrar a rota de cliente
app.register_blueprint(cliente_blueprint)

# cadastrar a rota de carros
app.register_blueprint(carros_blueprint)

# cadastrar a rota de Alerta de Falta de carro
app.register_blueprint(alertafaltacarro_blueprint)

app.run("0.0.0.0", port=8000, debug=False)

# cadastrar a rota de multa
app.register_blueprint(multas_blueprint)

# cadastrar a rota de multas por atraso
app.register_blueprint(multas_atraso_devolucao_blueprint)

#cadastrar a rota de multas por avaria
app.register_blueprint(multas_avaria_blueprint)

app.run("0.0.0.0", port=8000, debug=False)

