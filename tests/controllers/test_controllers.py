def test_rota_raiz(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "ok"}