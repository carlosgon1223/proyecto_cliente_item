# tests/test_api.py

import requests

def test_get_clientes():
    response = requests.get("http://localhost:8000/clientes/")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"

