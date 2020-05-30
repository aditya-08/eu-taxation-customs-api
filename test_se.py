from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_10_1():
    response = client.get("/tin/validate?countryCode=SE&tinNumber=640823-3234")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_10_2():
    response = client.get("/tin/validate?countryCode=SE&tinNumber=640883-3231")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_10_3():
    response = client.get("/tin/validate?countryCode=SE&tinNumber=610321-3499")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_10_3():
    response = client.get("/tin/validate?countryCode=SE&tinNumber=900102-2384")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_12_1():
    response = client.get("/tin/validate?countryCode=SE&tinNumber=19640823-3234")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_12_2():
    response = client.get("/tin/validate?countryCode=SE&tinNumber=19640883-3231")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True

def test_get_12_3():
    response = client.get("/tin/validate?countryCode=SE&tinNumber=19640883%2B3231")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True