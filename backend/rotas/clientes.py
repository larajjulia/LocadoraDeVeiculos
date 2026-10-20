# só vai ter as rotas
# vai receber as informações via API
# vai chamar o serviço de clientes

# fazendo uma rota pro Flask

from flask import Blueprint, jsonify, request
from servicos.clientes import ClienteDatabase

cliente_blueprint = Blueprint("cliente", __name__) # __name__ retorna o nome do módulo 

@cliente_blueprint.route("/cliente_registrar", methods=["POST"]) # HTTPS POST: atualizar um recurso
def post_cliente():
    json = request.get_json()
    nome = json.get("nome")
    cpf = json.get("cpf")
    telefones = json.get("telefones", []) # lista de telefones (atributo multivalorado)
    registro = ClienteDatabase().registra_cliente(nome, cpf, telefones)

    if not registro: # se deu problema ao criar registro (ex: excedeu o limite de caracteres)
        return jsonify("Não foi possível criar a conta"), 400 # Bad Request: não conseguiu processar a requisição

    return jsonify("Cadastro concluído com sucesso!"), 200