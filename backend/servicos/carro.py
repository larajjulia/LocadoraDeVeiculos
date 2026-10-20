from servicos.database.conector import DatabaseManager
class CarrosDoDatabase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_carros(self, categoria: str = "", locacao: str = "", cliente: str = ""):
        query = """
                SELECT * FROM carro c
                """
        if categoria: 
            query+= f"WHERE c.categoria = '{categoria}'\n"

        if locacao:
            if "WHERE" in query:
                query+= f"AND l.placa_veiculo_locacao = '{locacao}'\n"
            else:
                query+= f"WHERE l.placa_veiculo_locacao = '{locacao}'\n"

        if cliente:
                    if "WHERE" in query:
                        query+= f"AND cl.cpf = '{cliente}'\n"
                    else:
                        query+= f"WHERE cl.cpf = '{cliente}'\n"
        return self.db.execute_select_all(query)

# PARA SE RELACIONAR COM AS TABELAS LOCAÇÃO E CLIENTE:

# LEFT JOIN locacao l ON l.placa_veiculo_locacao = c.placa_veiculo
# LEFT JOIN cliente cl ON cl.cpf = l.cpf