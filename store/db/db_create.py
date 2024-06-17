import sqlite3
from store.db.db_client import DB_PATH


def create_db():
    conn = sqlite3.connect(DB_PATH)
    try:
        curr = conn.cursor()
        curr.execute('''CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            price REAL NOT NULL,
            quantity INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
        )''')

        curr.execute('''
            CREATE TRIGGER IF NOT EXISTS update_product_updated_at
            AFTER UPDATE ON products
            FOR EACH ROW
            BEGIN
                UPDATE products SET updated_at = CURRENT_TIMESTAMP WHERE id = OLD.id;
            END;
        ''')

        conn.commit()
    except Exception as err:
        raise err
    finally:
        conn.close()
