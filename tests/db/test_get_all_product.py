import pytest
from fastapi.testclient import TestClient
from store.main import app

from tests.fixtures import setup_db
from tests.factories import ProductIN_data

from store.db.db_client import SQLiteClient
from store.db.db_products import get_all_products_db, get_product_by_id_db, delete_product_db
from store.db.db_products import insert_product__db, update_product_db

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



def test_pegando_o_primeiro_item_do_db_pelo_id_deve_retornar_os_dados_do_primeiro_item(client, setup_db):
  test_db_client: SQLiteClient = setup_db

  primeiro_item_inserido = ProductIN_data()
  primeiro_item_db = get_product_by_id_db(test_db_client, 1)

  if primeiro_item_db:
    assert primeiro_item_db.name == primeiro_item_inserido["name"]
    assert primeiro_item_db.description == primeiro_item_inserido["description"]
    assert primeiro_item_db.price == primeiro_item_inserido["price"]
    assert primeiro_item_db.quantity == primeiro_item_inserido["quantity"]



def test_pegando_o_item_pelo_id_1_o_id_do_retorno_deve_ser_1(client, setup_db):
  test_db_client: SQLiteClient = setup_db
  primeiro_item_db = get_product_by_id_db(test_db_client, 1)

  if primeiro_item_db:
    assert primeiro_item_db.id == 1



def test_pegando_o_item_pelo_id_que_nao_existe_deve_retornar_none(client, setup_db):
  test_db_client: SQLiteClient = setup_db
  primeiro_item = get_product_by_id_db(test_db_client, 4)

  assert primeiro_item == None



def test_inserindo_um_novo_item_no_db(client, setup_db):
  test_db_client: SQLiteClient = setup_db

  produto = {
    "name": "produto2",
    "description": "produto2",
    "price": 0,
    "quantity": 0
  }

  produto_cadastrado = insert_product__db(
    test_db_client, 
    produto["name"], 
    produto["description"], 
    produto["price"], 
    produto["quantity"]
  )

  if produto_cadastrado:
    assert produto_cadastrado.id == 2
    assert produto_cadastrado.name == "produto2"



def test_atualizando_um_item_do_db_o_campo_updated_dev_atualizar(client, setup_db):
  test_db_client: SQLiteClient = setup_db

  produto = get_product_by_id_db(test_db_client, 2)

  novos_dados = {
    "name": "produto atualizado",
    "description": "produto atualizado",
    "price": 0,
    "quantity": 0
  }

  produto_atualizado = update_product_db(
    test_db_client,
    2, #id fo  item no banco
    novos_dados["name"], 
    novos_dados["description"], 
    novos_dados["price"], 
    novos_dados["quantity"]
  )

  if produto and produto_atualizado:
    assert produto.name != produto_atualizado.name



def test_deletenado_um_item_do_db(client, setup_db):
  test_db_client: SQLiteClient = setup_db

  delete_product_db(test_db_client, 1)
  teste = get_product_by_id_db(test_db_client, 1)

  assert teste == None