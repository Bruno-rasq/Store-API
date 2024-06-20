import pytest
from fastapi.testclient import TestClient

from tests.db.fixtures import setup_db
from store.db.db_client import SQLiteClient
from store.db.db_products import get_all_products_db
from store.main import app
from store.schemas.product import ProductOUT



@pytest.fixture()
def client():
  return TestClient(app)



def test_com_1_itens_cadastrados_no_db_a_lista_de_retorno_deve_ter_tamanho_1(client, setup_db):
  test_db_client: SQLiteClient = setup_db

  PRODUCTS = get_all_products_db(test_db_client)

  assert len(PRODUCTS) == 1


def test_retorno_de_todos_itens_do_db_deve_ser_uma_lista_de_productout(client, setup_db):
  test_db_client: SQLiteClient = setup_db

  PRODUCTS = get_all_products_db(test_db_client)

  assert all(isinstance(product, ProductOUT) for product in PRODUCTS)