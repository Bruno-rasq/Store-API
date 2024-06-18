import pytest
from pathlib import Path

from store.db.db_client import SQLiteClient
from tests.factories import ProductIN_data


TEST_DB_PATH = Path(__file__).parent / "test.db"


#TASK: criar metodos para criat um db teste, insierir um produto e excluir o db

def create_db_test(client: SQLiteClient):
  pass


#mudar nome da tabela
def insert_item_db_test(client: SQLiteClient, data):
  try:
    connection = client.get_connection()
    cursor = connection.cursor()
    cursor.execute('''
    INSERT INTO products (name, description, price, quantity)
    VALUES (?, ?, ?, ?)''', (
      data["name"], data["description"], data["price"], data["quantity"]
    ))
    client.client_commit()
  except Exception as err:
    raise err
  finally:
    client.close_connection()


#mudar nome da tabela
def drop_db_test(client: SQLiteClient):
  conn = client.get_connection()
  try:
    curr = conn.cursor()
    curr.execute('DROP TABLE products')
    client.client_commit()

  except Exception as err:
    raise err

  finally:
    client.close_connection()


@pytest.fixture(scope='module')
def setup_db():
  
  test_db_client = SQLiteClient(TEST_DB_PATH)
  data = ProductIN_data()

  create_db_test(test_db_client)
  insert_item_db_test(test_db_client, data)

  yield test_db_client

  drop_db_test(test_db_client)