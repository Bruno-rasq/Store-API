import sqlite3
from store.core.config import settings

class SQLiteClient:
  def __init__(self) -> None:
    self.connection = self.create_connection()

  def create_connection(self) -> sqlite3.Connection:
    try:
      conn = sqlite3.connect(settings.DATABASE_URL)
      return conn
    except sqlite3.Error as err:
      print(err)
      raise err

  def get(self) -> sqlite3.Connection:
    return self.connection


db_client = SQLiteClient()