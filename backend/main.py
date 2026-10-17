from __future__ import annotations
from typing import Any
import psycopg2
from psycopg2.extras import DictCursor
from flask import Flask, jsonify


class DatabaseManager:
    "Classe de Gerenciamento do database"

    def __init__(self) -> None:
        self.conn = psycopg2.connect(
            dbname="BD_Locadora_De_Veiculos",
            user="postgres",
            password="postgres",
            host="127.0.0.1",
            port=5432,
        )
        self.cursor = self.conn.cursor(cursor_factory=DictCursor)

    def execute_statement(self, statement: str) -> bool:
        "Usado para Inserções, Deleções, Alter Tables"
        try:
            self.cursor.execute(statement)
            self.conn.commit()
        except:
            self.conn.reset()
            return False
        return True

    def execute_select_all(self, query: str) -> list[dict[str, Any]]:
        "Usado para SELECTS no geral"
        self.cursor.execute(query)
        return [dict(item) for item in self.cursor.fetchall()]

    def execute_select_one(self, query: str) -> dict | None:
        "Usado para SELECT com apenas uma linha de resposta"
        self.cursor.execute(query)
        query_result = self.cursor.fetchone()

        if not query_result:
            return None

        return dict(query_result)

db = DatabaseManager()
carro = (db.execute_select_all("SELECT * from carro"))
print(carro)
app = Flask(__name__) 

@app.route("/carro", methods=["GET"])
def get_carro():
    return jsonify(carro), 200

app.run("0.0.0.0", port=8000, debug=False)