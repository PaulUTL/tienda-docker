import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

def test_inicio():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "Tienda DevOps 1.0"}

def test_calcular_compra_valida():
    data = {"precio": 100, "descuento": 10}
    response = client.post("/compra", json=data)
    assert response.status_code == 200
    assert response.json()["subtotal"] == pytest.approx(90.0)
    assert response.json()["total"] == pytest.approx(104.4)

def test_calcular_compra_precio_negativo():
    data = {"precio": -100, "descuento": 10}
    response = client.post("/compra", json=data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Precio invalido"

def test_calcular_compra_descuento_invalido():
    data = {"precio": 100, "descuento": 150}
    response = client.post("/compra", json=data)
    assert response.status_code == 400
    assert response.json()["detail"] == "Descuento invalido"

def test_version():
    respuesta = client.get("/version")
    assert respuesta.status_code == 200
    assert respuesta.json()["version"] == "1.1.0"

def test_revision():
    respuesta = client.get("/revision")
    assert respuesta.status_code == 200
    assert respuesta.json()["estado"] == "ok"