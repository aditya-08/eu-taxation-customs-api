from fastapi.testclient import TestClient
from main import app

import requests

client = TestClient(app)

baseUrl="http://localhost:8000/tin/validate?countryCode=RO&tinNumber="

def test_get_1():
    response = client.get("/tin/validate?countryCode=RO&tinNumber=8001011234567")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=RO&tinNumber=8001011534567")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_3():
    url = baseUrl + "8001011534567"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
