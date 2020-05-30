from fastapi.testclient import TestClient
from main import app

import requests

client = TestClient(app)

baseUrl="http://localhost:8000/tin/validate?countryCode=PT&tinNumber="

def test_get_1():
    response = client.get("/tin/validate?countryCode=PT&tinNumber=299999998")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=PT&tinNumber=29999999")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_3():
    url = baseUrl + "299999998"
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
