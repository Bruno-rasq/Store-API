import pytest
from pydantic import ValidationError
from typing import Any
from datetime import datetime
from store.schemas.product import ProductIN, ProductOUT
from tests.factories import ProductIN_data


def test_productIN_em_formato_valido():
  data = ProductIN_data()
  product = ProductIN(
    name        = data["name"],
    description = data["description"],
    price       = data["price"],
    quantity    = data["quantity"]
  )
  assert product.name        == "produto teste"
  assert product.description == "produto teste"
  assert product.price       == 20.0
  assert product.quantity    == 10


def test_productIN_com_campo_price_invalido():
  invalid_price: Any = "20.0"
  try:
    ProductIN(
      name        = "produto teste",
      description = "produto teste",
      price       = invalid_price,
      quantity    = 10
    )
  except ValidationError as err:
    print(err)
    print(err.errors())
    assert any(error['loc'] == ('price', ) and error['type'] == 'type_error.float' for error in err.errors())
    raise


@pytest.mark.xfail(raises=ValidationError)
def test_productIN_sem_campo_price():
  produto = ProductIN(name="teste", description="teste", quantity=20)
  # with pytest.raises(ValidationError) as err:
  #   ProductIN(
  #     name        = "produto teste",
  #     description = "produto teste",
  #     quantity    = 10
  #   )
  # assert "price" in str(err.value)


def test_productOUT_em_formato_valido():
  data = ProductIN_data()
  product = ProductOUT(
    id = 1,
    name        = data["name"],
    description = data["description"],
    price       = data["price"],
    quantity    = data["quantity"],
    created_at  = datetime(2024, 6, 18, 14, 49),
    updated_at  = datetime(2024, 6, 18, 14, 49),
  )

  assert product.name        == "produto teste"
  assert product.description == "produto teste"
  assert product.price       == 20.0
  assert product.quantity    == 10
  assert product.id          == 1
  assert product.created_at  == datetime(2024, 6, 18, 14, 49)
  assert product.updated_at  == datetime(2024, 6, 18, 14, 49)


def test_productOUT_sem_campos_opcionais():
  data = ProductIN_data()
  product = ProductOUT(
    name        = data["name"],
    description = data["description"],
    price       = data["price"],
    quantity    = data["quantity"],
  )

  assert product.id is None 
  assert product.created_at is None
  assert product.updated_at is None