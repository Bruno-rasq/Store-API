import sqlite3
from pathlib import Path
#from store.core.config import settings

root_path = Path(__file__).parent

def setup_database():
  conn = sqlite3.connect(root_path / 'Products.db')
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Produtos (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT NOT NULL,
      quantity INTEGER NOT NULL,
      price REAL NOT NULL,
      status BOOLEAN NOT NULL
    )
    ''')
  conn.commit()
  conn.close()


if __name__ == "__main__":
  setup_database()