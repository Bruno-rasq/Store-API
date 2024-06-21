from fastapi import status


def test_rota_raiz(client):
  response = client.get("/")
  assert response.status_code == status.HTTP_200_OK
  assert response.json() == {"message": "ok"}


# @pytest.mark.controllers
# def test_rota_get_padrao(client, product_url):
#   response = client.get(product_url)
#   assert response.status_code == status.HTTP_200_OK