from servicos.database.conector import DatabaseManager
class CarrosDoDatabase():
    def __init__(self, db_provider = DatabaseManager()) -> None:
        self.db = db_provider

    def get_carros(self):
        query = """
                SELECT * FROM carro
                """
        return self.db.execute_select_all(query)