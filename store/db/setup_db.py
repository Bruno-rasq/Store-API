from store.db.client import db_client

def setup_database():
  conn = db_client.get()
  cursor = conn.cursor()
  cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products (
      id TEXT PRIMARY KEY,
      created_at TEXT,
      updated_at TEXT,
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