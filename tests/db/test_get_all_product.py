import pytest
from fastapi.testclient import TestClient

from store.db.db_client import SQLiteClient
from store.db.db_products import get_all_products_db
from store.main import app
from tests.db.fixtures import setup_db


@pytest.fixture()
def client():
  return TestClient(app)

def test_get_all_products_sucess(client, setup_db):
  db_client: SQLiteClient = setup_db

  PRODUCTS = get_all_products_db(db_client)

  assert len(PRODUCTS) == 1
  assert dict(PRODUCTS[0])["name"] == "produto teste"
  assert dict(PRODUCTS[0])["description"] == "produto teste"
  assert dict(PRODUCTS[0])["price"] == 20.0
  assert dict(PRODUCTS[0])["quantity"] == 10
  