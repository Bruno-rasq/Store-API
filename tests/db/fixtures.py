import pytest

from tests.factories import ProductIN_data
from store.db.db_client import db_client
from store.db.db_products import insert_product__db
from store.db.db_create import drop_db_test, create_db


@pytest.fixture(scope='module')
def setup_db():
  
  data = ProductIN_data()

  create_db(db_client)
  insert_product__db(db_client, data["name"], data["description"], data["price"], data["quantity"])

  yield db_client

  drop_db_test(db_client)