from store.db.db_client import SQLiteClient


def create_db(client: SQLiteClient):
    conn = client.get_connection()
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

        client.client_commit()

    except Exception as err:
        raise err

    finally:
        client.close_connection()