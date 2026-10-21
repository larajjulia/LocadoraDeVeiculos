from servicos.database.conector import DatabaseManager
class CarrosDoDatabase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_carros(self, categoria: str = "", cliente: str = "", locacao: str = ""):
        query = """
                SELECT c.*,
                l.cnh,
                l.valor_locacao,
                l.hora_locacao::text AS hora_locacao,
                l.data_retirada::text AS data_retirada,
                l.data_devolucao_prevista::text AS data_devolucao_prevista,
                l.data_devolucao_efetiva::text AS data_devolucao_efetiva,
                l.id_locacao,
                l.cpf,
                l.placa_veiculo_locacao
                FROM carro c                 
                LEFT JOIN locacao l ON c.placa_veiculo = l.placa_veiculo_locacao
                LEFT JOIN cliente cl ON cl.cpf = l.cpf
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

    def registra_carro(self,categoria, placa_veiculo, modelo, quilometragem, estado, valor_seguro, valor_diaria):
        statement = f"INSERT INTO carro (categoria, placa_veiculo, modelo, quilometragem, estado, valor_seguro, valor_diaria) VALUES ('{categoria}', '{placa_veiculo}', '{modelo}', {quilometragem}, '{estado}', {valor_seguro}, {valor_diaria})"
        self.db.execute_statement(statement)