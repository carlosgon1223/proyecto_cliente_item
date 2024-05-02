# tests/test_api.py

import requests

def test_get_clientes():
    # Prueba la ruta GET /clientes/ y verifica que devuelva un código de estado 200
    # y que la respuesta contenga datos válidos en formato JSON.
    response = requests.get("http://localhost:8000/clientes/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    # Agrega más aserciones según sea necesario.

# Agrega más pruebas de integración según sea necesario.
