import pytest
from app import app

@pytest.fixture
def client():
    app.testing = True
    with app.app_context():
        with app.test_client() as client:
            yield client

# --- Test de la página HTML ---
def test_home_html(client):
    response = client.get("/")
    assert response.status_code == 200

   contenido = response.get_data(as_text=True).lower()
  assert "🚀 Mini erick silva" in contenido


# --- Tests del endpoint /saludar ---
def test_saludar_ok(client):
    response = client.post("/saludar", json={"nombre": "Erick"})
    data = response.get_json()

    assert response.status_code == 200
    assert "mensaje" in data
    assert "erick" in data["mensaje"].lower()

def test_saludar_error(client):
    response = client.post("/saludar", json={})
    assert response.status_code == 400

# --- Tests del endpoint /ia ---
def test_ia_ok(client):
    response = client.post("/ia", json={"texto": "hola"})
    data = response.get_json()

    assert response.status_code == 200
    assert "resultado" in data
    assert "parece" in data["resultado"].lower()

def test_ia_error(client):
    response = client.post("/ia", json={})
    assert response.status_code == 400
