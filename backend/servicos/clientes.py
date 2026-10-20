# o serviço de "clientes" vai ficar fazendo consultas no nosso database
# para retornar ou cadastrar pra gente o que a gente precisa

from servicos.database.conector import DatabaseManager

# nossa rota vai chamar o método registra_cliente dessa classe

class ClienteDatabase():
        def __init__(self, db_provider = DatabaseManager()) -> None:
                self.db = db_provider

        # Função para adicionar registros na tabela Cliente
        # telefones é um vetor de strings, uma vez que é atributo multivalorado
        # A função retorna true se a execução de ambos os comandos do SQL forem
        # bem sucedidas
        def registra_cliente(self, nome: str, cpf: str, telefones: str) -> bool:
                statement = f"INSERT INTO cliente (nome, cpf) VALUES ('{nome}', '{cpf}')\n"
                ok = self.db.execute_statement(statement)

                # atributo multivalorado
                for tel in telefones:
                        statement2 = f"INSERT INTO telefone (numero, cpf) VALUES ('{tel}', '{cpf}')\n"
                        ok2 = self.db.execute_statement(statement2)

                return ok and ok2