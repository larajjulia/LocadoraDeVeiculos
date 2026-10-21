from servicos.database.conector import DatabaseManager

class LocacaoDatabase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_locacao(self, cpf: str = ""):     
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
        params = []

        if cpf:
            query += f" WHERE cliente.cpf = '{cpf}'"

        # if carro:
        #     if "WHERE" in query:
        #         query += " AND carro.placa_veiculo = %s"
        #     else:
        #         query += " WHERE carro.placa_veiculo = %s"
        #     params.append(carro)

        # if id_locacao:
        #     if "WHERE" in query:
        #         query += " AND l.id_locacao = %s"
        #     else:
        #         query += " WHERE l.id_locacao = %s"
        #     params.append(id_locacao)

        # if data_retirada:
        #     if "WHERE" in query:
        #         query += " AND l.data_retirada = %s"
        #     else:
        #         query += " WHERE l.data_retirada = %s"
        #     params.append(data_retirada)

        return self.db.execute_select_all(query)

                # SELECT * FROM locacao l
                # LEFT JOIN cliente  ON cliente.cpf = l.cpf
                # LEFT JOIN carro ON carro.placa_veiculo = l.placa_veiculo_locacao
