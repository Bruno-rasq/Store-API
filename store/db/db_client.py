import sqlite3
from pathlib import Path
from threading import local

DB_PATH = Path(__file__).parent / "produtos.db"

class SQLiteClient:
    def __init__(self) -> None:
        self.local = local()

    def create_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(DB_PATH)

    def get_connection(self):
        if not hasattr(self.local, 'connection'):
            self.local.connection = self.create_connection()
        return self.local.connection

    def close_connection(self):
        if hasattr(self.local, 'connection'):
            self.local.connection.close()
            del self.local.connection

    def client_commit(self):
        if hasattr(self.local, 'connection'):
            self.local.connection.commit()


db_client = SQLiteClient()