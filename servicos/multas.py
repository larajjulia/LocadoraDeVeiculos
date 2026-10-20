from servicos.database.conector import DatabaseManager

class MultasDataBase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_multas(self, id_locacao: int = None):
        query = """   
                SELECT m.*,
                        l.cnh,
                        l.valor_locacao,
                        l.hora_locacao::text AS hora_locacao,
                        l.data_retirada::text AS data_retirada,
                        l.data_devolucao_prevista::text AS data_devolucao_prevista,
                        l.data_devolucao_efetiva::text AS data_devolucao_efetiva,
                        l.id_locacao,
                        l.cpf,
                        l.placa_veiculo_locacao
                FROM multa m                 
                LEFT JOIN locacao l ON l.id_Locacao = m.id_multa
                """

        if id_locacao:
            query+= f" WHERE l.id_locacao = {id_locacao}"
                
        return self.db.execute_select_all(query)

    def registra_multa(self, valor_multa, status, id_multa):

        statement = f"INSERT INTO multa(valor_multa, status, id_multa) VALUES ('{valor_multa}', '{status}', '{id_multa}')"
        self.db.execute_statement(statement)