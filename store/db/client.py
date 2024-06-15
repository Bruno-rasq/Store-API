import sqlite3
from pathlib import Path

DATABASE_PATH = Path(__file__).parent / "produtos.db"

class SQLiteClient:
  def __init__(self) -> None:
    self.connection = self.create_connection()

  def create_connection(self) -> sqlite3.Connection:
    try:
      conn = sqlite3.connect(DATABASE_PATH)
      return conn
    except sqlite3.Error as err:
      print(err)
      raise err

  def get(self) -> sqlite3.Connection:
    return self.connection

  def cursor(self) -> sqlite3.Cursor:
    return self.connection.cursor()

  def commit(self) -> None:
    self.connection.commit()

  def close(self) -> None:
    if self.connection:
      self.connection.close()

db_client = SQLiteClient()