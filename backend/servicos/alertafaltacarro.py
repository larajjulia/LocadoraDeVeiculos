from servicos.database.conector import DatabaseManager

class AlertaFaltaCarroDatabase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
            self.db = db_provider

    def get_alertafaltacarro(self):

        query = "SELECT * FROM carro WHERE estado IN ('Manutenção')"
        return self.db.execute_select_all(query)