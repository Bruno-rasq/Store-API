import uuid
from typing import List
from datetime import datetime
from store.db.client import db_client
from store.schemas.product import ProductOUT, ProductIn


#TASK: criar metodo para cadastrar um novo produto no banco de dados.
def cadastrar_produto_db(prod: ProductIn) -> ProductOUT:
  conn = db_client.get()
  curr = conn.cursor()

  product_id = uuid.uuid4()
  product_created_at = datetime.utcnow().isoformat()
  product_updated_at = product_created_at
  
  curr.execute('''
  INSERT INTO Products (id, created_at, updated_at, name, quantity, price, status)
  VALUES (?, ?, ?, ?, ?, ?, ?)''', 
  (str(product_id), product_created_at, product_updated_at, prod.name, prod.quantity, prod.price, prod.status)
  )

  conn.commit()
  conn.close()

  product = ProductOUT(
    id=product_id,
    created_at=datetime.fromisoformat(product_created_at),
    updated_at=datetime.fromisoformat(product_updated_at),
    name=prod.name,
    quantity=prod.quantity,
    price=prod.price,
    status=prod.status
  )
  return product 


#TASK: criar metodo para pegar todos os produtos cadastrados no banco de dados.
def get_produtos_db() -> List[ProductOUT]:
  conn = db_client.get()
  curr = conn.cursor()
  curr.execute('''SELECT * FROM Products''')
  rows = curr.fetchall()
  products = []
  for row in rows:
    product = ProductOUT(
      id=row[0],
      created_at=datetime.fromisoformat(row[1]),
      updated_at=datetime.fromisoformat(row[2]),
      name=row[3],
      quantity=row[4],
      price=row[5],
      status=row[6]
    )
    products.append(product)
  conn.close()
  return products
  

#TASK: criar metodo para pegar um produto do banco de dados pelo seu id.
# def get_produto_db():
#   conn = db_client.get()
#   curr = conn.cursor()
#   pass

#TASK: criar metodo para atualizar os dados de um produto.
# def update_produto_db():
#   conn = db_client.get()
#   curr = conn.cursor()
#   pass

#TASK: criar metodo para deletar um produto do banco de dados.
# def delete_produto_db():
#   conn = db_client.get()
#   curr = conn.cursor()
#   pass