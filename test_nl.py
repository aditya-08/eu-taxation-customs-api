from fastapi.testclient import TestClient
from main import app

import requests

client = TestClient(app)

baseUrl="http://localhost:8000/tin/validate?countryCode=NL&tinNumber="

def test_get_1():
    response = client.get("/tin/validate?countryCode=NL&tinNumber=174559434")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=NL&tinNumber=17455943")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_3():
    url = baseUrl + "174559434"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True
