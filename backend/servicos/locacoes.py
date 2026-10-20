from servicos.database.conector import DatabaseManager

class LocacaoDatabase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_locacao(self, cpf: str = "", carro: str = "", id_locacao: int | None = None, data_retirada: str = ""):     
        query = """ 
              
                SELECT * FROM locacao l
                LEFT JOIN cliente  ON cliente.cpf = l.cpf
                LEFT JOIN carro ON carro.placa_veiculo = l.placa_veiculo_locacao

                """
        params = []

        if cpf:
            query += " WHERE cliente.cpf = %s"
            params.append(cpf)

        if carro:
            if "WHERE" in query:
                query += " AND carro.placa_veiculo = %s"
            else:
                query += " WHERE carro.placa_veiculo = %s"
            params.append(carro)

        if id_locacao:
            if "WHERE" in query:
                query += " AND l.id_locacao = %s"
            else:
                query += " WHERE l.id_locacao = %s"
            params.append(id_locacao)

        if data_retirada:
            if "WHERE" in query:
                query += " AND l.data_retirada = %s"
            else:
                query += " WHERE l.data_retirada = %s"
            params.append(data_retirada)

        return self.db.execute_select_all(query, params)
    