from client import db_client

#TASK: criar metodo para cadastrar um novo produto no banco de dados.
def cadastrar_produto_db():
  conn = db_client.get()
  curr = conn.cursor()
  pass

#TASK: criar metodo para pegar todos os produtos cadastrados no banco de dados.
def get_produto_db():
  conn = db_client.get()
  curr = conn.cursor()
  pass

#TASK: criar metodo para pegar um produto do banco de dados pelo seu id.
def get_produtos_db():
  conn = db_client.get()
  curr = conn.cursor()
  pass

#TASK: criar metodo para atualizar os dados de um produto.
def update_produto_db():
  conn = db_client.get()
  curr = conn.cursor()
  pass

#TASK: criar metodo para deletar um produto do banco de dados.
def delete_produto_db():
  conn = db_client.get()
  curr = conn.cursor()
  pass