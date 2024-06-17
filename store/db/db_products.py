from store.db.db_client import db_client


#[GET]
def get_all_products_db():
  conn = db_client.get_connection()
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
      return products

  except Exception as err:
      raise err

  finally:
      db_client.close_connection()


#[GET]
def get_product_by_id_db(product_id):
  conn = db_client.get_connection()
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
      return product

  except Exception as err:
      raise err

  finally:
      db_client.close_connection()


#[POST]
def insert_product__db(name: str, description: str, price: float, quantity: int):
  conn = db_client.get_connection()
  try:
    curr = conn.cursor()
    curr.execute(
      '''
      INSERT INTO products (name, description, price, quantity)
      VALUES (?, ?, ?, ?)
      ''', (name, description, price, quantity)
    )
    db_client.client_commit()

  except Exception as err:
    raise err

  finally:
    db_client.close_connection()


#[PUT]
def update_product_db(product_id, name, description, price, quantity):
  conn = db_client.get_connection()
  try:
      curr = conn.cursor()
      curr.execute('''
          UPDATE products
          SET name = ?, description = ?, price = ?, quantity = ?, updated_at = CURRENT_TIMESTAMP
          WHERE id = ?
      ''', (name, description, price, quantity, product_id))
      db_client.client_commit()

  except Exception as err:
      raise err

  finally:
      db_client.close_connection()


#[DELETE]
def delete_product_db(product_id):
  conn = db_client.get_connection()
  try:
      curr = conn.cursor()
      curr.execute('DELETE FROM products WHERE id = ?', (product_id,))
      db_client.client_commit()

  except Exception as err:
      raise err

  finally:
      db_client.close_connection()