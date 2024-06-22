from store.schemas.product import ProductOUT 
from typing import List, Optional
from store.db.db_client import SQLiteClient, db_client

#[GET]
def get_all_products_db(client: SQLiteClient) -> List[ProductOUT]:
  conn = client.get_connection()
  try:
      curr = conn.cursor()
      curr.execute('SELECT * FROM products')
      rows = curr.fetchall()
      products = []
      for row in rows:
          product = ProductOUT(
              id          = row[0],
              name        = row[1],
              description = row[2],
              price       = row[3],
              quantity    = row[4],
              created_at  = row[5],
              updated_at  = row[6]
          )
          products.append(product)
      return products

  except Exception as err:
      raise err

  finally:
      client.close_connection()


#[GET]
def get_product_by_id_db(client: SQLiteClient, product_id) -> Optional[ProductOUT]:
  conn = client.get_connection()
  try:
      curr = conn.cursor()
      curr.execute('SELECT * FROM products WHERE id = ?', (product_id,))
      row = curr.fetchone()
      if row:
          product = ProductOUT(
              id          = row[0],
              name        = row[1],
              description = row[2],
              price       = row[3],
              quantity    = row[4],
              created_at  = row[5],
              updated_at  = row[6]
          )
      else:
          product = None
      return product

  except Exception as err:
      raise err

  finally:
      client.close_connection()


#[POST]
def insert_product__db(client: SQLiteClient, name: str, description: str, price: float, quantity: int):
  conn = client.get_connection()
  try:
    curr = conn.cursor()
    curr.execute(
      '''
      INSERT INTO products (name, description, price, quantity)
      VALUES (?, ?, ?, ?)
      ''', (name, description, price, quantity)
    )
    client.client_commit()
    id = curr.lastrowid
    return get_product_by_id_db(db_client, id)

  except Exception as err:
    raise err

  finally:
    client.close_connection()


#[PUT]
def update_product_db(client: SQLiteClient, product_id, name, description, price, quantity):
  conn = client.get_connection()
  try:
      curr = conn.cursor()
      curr.execute('''
          UPDATE products
          SET name = ?, description = ?, price = ?, quantity = ?, updated_at = CURRENT_TIMESTAMP
          WHERE id = ?
      ''', (name, description, price, quantity, product_id))
      client.client_commit()

      return get_product_by_id_db(db_client, product_id)

  except Exception as err:
      raise err

  finally:
      client.close_connection()


#[DELETE]
def delete_product_db(client: SQLiteClient, product_id):
  conn = client.get_connection()
  try:
      curr = conn.cursor()
      curr.execute('DELETE FROM products WHERE id = ?', (product_id,))
      client.client_commit()
      row_affect = curr.rowcount
      return row_affect > 0
    
  except Exception as err:
      raise err

  finally:
      client.close_connection()