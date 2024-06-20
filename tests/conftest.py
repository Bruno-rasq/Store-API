import pytest
import os
from fastapi.testclient import TestClient

from store.main import app
from tests.factories import ProductIN_data
from store.db.db_client import db_client, DB_PATH
from store.db.db_products import insert_product__db
from store.db.db_create import create_db

@pytest.fixture()
def client():
  return TestClient(app)

@pytest.fixture(scope='module')
def setup_db():
  
  data = ProductIN_data()

  create_db(db_client)
  insert_product__db(db_client, data["name"], data["description"], data["price"], data["quantity"])

  yield db_client

  if os.path.exists(DB_PATH):
    os.remove(DB_PATH)


@pytest.fixture
def product_url():
  return "/products/"