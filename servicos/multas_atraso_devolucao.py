from servicos.database.conector import DatabaseManager

class Multas_Atraso_DevolucaoDataBase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_multas_atraso_devolucao(self, id_multa: int = None):
        query = """   
                SELECT ma.*,
                        m.valor_multa,
                        m.status,
                        l.cnh,
                        l.valor_locacao,
                        l.hora_locacao::text AS hora_locacao,
                        l.data_retirada::text AS data_retirada,
                        l.data_devolucao_prevista::text AS data_devolucao_prevista,
                        l.data_devolucao_efetiva::text AS data_devolucao_efetiva,
                        l.id_locacao,
                        l.cpf,
                        l.placa_veiculo_locacao
                FROM multa_atraso_devolucao ma
                LEFT JOIN multa m ON m.id_multa  = ma.id_multa_atraso_devolucao
                LEFT JOIN locacao l ON l.id_locacao = m.id_multa
                """

        if id_multa:
            query+= f" WHERE ma.id_multa_atraso_devolucao = {id_multa}"
                
        return self.db.execute_select_all(query)

    def registra_multa_atraso_devolucao(self, id_multa_atraso_devolucao):
    
            statement = f"INSERT INTO multa_atraso_devolucao(id_multa_atraso_devolucao) VALUES ('{id_multa_atraso_devolucao}')"
            self.db.execute_statement(statement)
