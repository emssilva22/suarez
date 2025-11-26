import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    return app.test_client()

# --- Test de la página HTML ---
def test_home_html(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "<html" in response.get_data(as_text=True).lower()
    assert "mini ia flask" in response.get_data(as_text=True)

# --- Tests del endpoint /saludar ---
def test_saludar_ok(client):
    response = client.post("/saludar", json={"nombre": "Erick"})
    data = response.get_json()

    assert response.status_code == 200
    assert "mensaje" in data
    assert "Erick" in data["mensaje"]

def test_saludar_error(client):
    response = client.post("/saludar", json={})
    assert response.status_code == 400

# --- Tests del endpoint /ia ---
def test_ia_ok(client):
    response = client.post("/ia", json={"texto": "hola"})
    data = response.get_json()

    assert response.status_code == 200
    assert "resultado" in data

def test_ia_error(client):
    response = client.post("/ia", json={})
    assert response.status_code == 400
