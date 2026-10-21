from servicos.database.conector import DatabaseManager

class LocacaoDatabase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_locacao(self, cpf: str = "", placa_veiculo: str = "", id_locacao: int | None = None, data_retirada: str = ""):     
        query= """ 
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


        if cpf:
            query += f" WHERE cl.cpf = '{cpf}'"


        if placa_veiculo:
            if "WHERE" in query:
                query+= f"AND c.placa_veiculo = '{placa_veiculo}'\n"
            else:
                query+= f"WHERE c.placa_veiculo = '{placa_veiculo}'\n"


        if id_locacao:
            if "WHERE" in query:
                query+= f"AND l.id_locacao = '{id_locacao}'\n"
            else:
                query+= f"WHERE l.id_locacao = '{id_locacao}'\n"

        

        if data_retirada:
            if "WHERE" in query:
                query+= f"AND l.data_retirada = '{data_retirada}'\n"
            else:
                query+= f"WHERE l.data_retirada = '{data_retirada}'\n"

      

        return self.db.execute_select_all(query)


    def registra_locacao(self,cnh, valor_locacao, hora_locacao, data_retirada, data_devolucao_prevista, data_devolucao_efetiva, id_locacao, cpf, placa_veiculo_locacao):
            statement = f"INSERT INTO locacao (cnh, valor_locacao, hora_locacao, data_retirada, data_devolucao_prevista, data_devolucao_efetiva, id_locacao, cpf, placa_veiculo_locacao) VALUES ('{cnh}', '{valor_locacao}', '{valor_locacao}', {data_retirada}, '{data_devolucao_prevista}', {data_devolucao_efetiva}, {id_locacao}, {cpf}, {placa_veiculo_locacao})"
            self.db.execute_statement(statement)