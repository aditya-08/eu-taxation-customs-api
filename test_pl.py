from fastapi.testclient import TestClient
from main import app

import requests

client = TestClient(app)

baseUrl="http://localhost:8000/tin/validate?countryCode=PL&tinNumber="

def test_get_1():
    response = client.get("/tin/validate?countryCode=PL&tinNumber=2234567895")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=PL&tinNumber=223456789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_3():
    url = baseUrl + "2234567895"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_11_1():
    response = client.get("/tin/validate?countryCode=PL&tinNumber=02070803628")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_11_2():
    response = client.get("/tin/validate?countryCode=PL&tinNumber=02070803627")
    assert response.status_code == 200
    assert response.json()["validSyntax"] == False

def test_get_11_3():
    url = baseUrl + "02070803628"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True
