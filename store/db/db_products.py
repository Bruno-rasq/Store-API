import sqlite3
from store.db.db_client import DB_PATH


#[GET]
def get_all_products_db():
  conn = sqlite3.connect(DB_PATH)
  try:
      curr = conn.cursor()
      curr.execute('SELECT * FROM products')
      rows = curr.fetchall()
      products = []
      for row in rows:
          product = {
              "id"          : row[0],
              "name"        : row[1],
              "description" : row[2],
              "price"       : row[3],
              "quantity"    : row[4],
              "created_at"  : row[5],
              "updated_at"  : row[6]
          }
          products.append(product)
      conn.close()
      return products
  except Exception as err:
      raise err
  finally:
      conn.close()


#[GET]
def get_product_by_id_db(product_id):
  conn = sqlite3.connect(DB_PATH)
  try:
      curr = conn.cursor()
      curr.execute('SELECT * FROM products WHERE id = ?', (product_id,))
      row = curr.fetchone()
      if row:
          product = {
              "id"          : row[0],
              "name"        : row[1],
              "description" : row[2],
              "price"       : row[3],
              "quantity"    : row[4],
              "created_at"  : row[5],
              "updated_at"  : row[6]
          }
      else:
          product = None
      conn.close()
      return product
  except Exception as err:
      raise err
  finally:
      conn.close()


#[POST]
def insert_product__db(name: str, description: str, price: float, quantity: int):
  conn = sqlite3.connect(DB_PATH)
  try:
    curr = conn.cursor()
    curr.execute(
      '''
      INSERT INTO products (name, description, price, quantity)
      VALUES (?, ?, ?, ?)
      ''', (name, description, price, quantity)
    )
    conn.commit()

  except Exception as err:
    raise err
  finally:
    conn.close()


#[PUT]
def update_product_db(product_id, name, description, price, quantity):
  conn = sqlite3.connect(DB_PATH)
  try:
      curr = conn.cursor()
      curr.execute('''
          UPDATE products
          SET name = ?, description = ?, price = ?, quantity = ?, updated_at = CURRENT_TIMESTAMP
          WHERE id = ?
      ''', (name, description, price, quantity, product_id))
      conn.commit()
  except Exception as err:
      raise err
  finally:
      conn.close()


#[DELETE]
def delete_product_db(product_id):
  conn = sqlite3.connect(DB_PATH)
  try:
      curr = conn.cursor()
      curr.execute('DELETE FROM products WHERE id = ?', (product_id,))
      conn.commit()
  except Exception as err:
      raise err
  finally:
      conn.close()