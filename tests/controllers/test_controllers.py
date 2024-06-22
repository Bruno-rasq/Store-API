from fastapi import status


def test_rota_raiz_deve_retornar_status_code_200_e_msg_ok(client):
  response = client.get("/")
  assert response.status_code == status.HTTP_200_OK
  assert response.json() == {"message": "ok"}


def test_rota_get_deve_retornar_status_code_200_ok(client):
  result = client.get("/products/")

  assert result.status_code == status.HTTP_200_OK


def test_rota_get_deve_retornar_um_objeto_que_contenha_product(client):
  result = client.get("/products/")

  assert result.json() == { "products": [] }


def test_rota_post_deve_retornar_status_code_201_created(client):
  response = client.post(
    "/products/", 
    json = {
      'name': 'produto teste',
      'description': '',
      'price': 0,
      'quantity': 0
    },
  )

  assert response.status_code == status.HTTP_201_CREATED


def test_rota_put_deve_retornar_status_code_200_ok(client):
  result = client.put(
    "/products/1", 
    json = {
      'name': 'produto updated',
      'description': '',
      'price': 0,
      'quantity': 0
    },
  )

  assert result.status_code == status.HTTP_200_OK


def test_rota_delete_deve_retornar_status_code_204_no_content(client):
  result = client.delete("/products/1")

  assert result.status_code == status.HTTP_204_NO_CONTENT