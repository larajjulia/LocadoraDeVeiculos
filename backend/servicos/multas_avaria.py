from servicos.database.conector import DatabaseManager

class Multas_AvariaDataBase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_multas_avaria(self, id_multa: int = None):
        query = """   
                SELECT mav.*,
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
                FROM multa_avaria mav
                LEFT JOIN multa m ON m.id_multa  = mav.id_multa_avaria
                LEFT JOIN locacao l ON l.id_locacao = m.id_multa
                """

        if id_multa:
            query+= f" WHERE mav.id_multa_avaria = {id_multa}"
                
        return self.db.execute_select_all(query)


    def registra_multa_avaria(self, id_multa_avaria, grau):

        statement = f"INSERT INTO multa_avaria(id_multa_avaria, grau) VALUES ('{id_multa_avaria}', '{grau}')"
        self.db.execute_statement(statement)
