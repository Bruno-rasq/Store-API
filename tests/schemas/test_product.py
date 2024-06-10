from store.schemas.product import ProductIn
from uuid import UUID
import pytest
from pydantic import ValidationError
from tests.schemas.factories import Product_data

def test_schemas_return_sucess():
  data = Product_data()
  product = ProductIn(**data)

  assert product.name == "produto teste"
  assert isinstance(product.id, UUID)

def test_schemas_return_raise():
  data = {"name": "produto teste", "quantity": 10, "price": 20}

  with pytest.raises(ValidationError) as err:
    ProductIn(**data)

  assert err.value.errors()[0] == {
    'type': 'missing', 
    'loc': ('status',), 
    'msg': 'Field required', 
    'input': {'name': 'produto teste', 'quantity': 10, 'price': 20.0}, 
    'url': 'https://errors.pydantic.dev/2.7/v/missing'
  }
    