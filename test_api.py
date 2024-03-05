"""Application : test api de Crédit Score

Network URL: http://192.168.1.20:8501
Lancement en local depuis une console anaconda prompt : 
    streamlit run test_api.py
"""

import pytest
from fastapi.testclient import TestClient
from api import app

client = TestClient(app)

# Test de l'endpoint greet
def test_greet():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "bonjours"}

# Test de l'endpoint get_client_ids
def test_get_client_ids():
    response = client.get("/client_ids/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test de l'endpoint get_client_info
def test_get_client_info():
    client_id = 123456  # Remplacez par un ID client existant
    response = client.get(f"/client_info/{client_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "client_info" in response.json()

# Test de l'endpoint get_client_pret
def test_get_client_pret():
    client_id = 123456  # Remplacez par un ID client existant
    response = client.get(f"/client_pret/{client_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "client_pret" in response.json()

# Test de l'endpoint get_client_scores
def test_get_client_scores():
    client_id = 123456  # Remplacez par un ID client existant
    response = client.get(f"/client_scores/{client_id}")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert all(key in response.json() for key in ["score_client", "score_moy_voisins_test", "pourc_def_voisins_train", "pourc_def_voisins_test"])
