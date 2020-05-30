from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_1():
    response = client.get("/tin/validate?countryCode=AT&tinNumber=931736581")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=AT&tinNumber=93173/6581")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_3():
    response = client.get("/tin/validate?countryCode=AT&tinNumber=9317365")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False

def test_get_4():
    response = client.get("/tin/validate?countryCode=AT&tinNumber=93173658A")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False

def test_get_5():
    response = client.get("/tin/validate?countryCode=AT&tinNumber=931736")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False

def test_get_6():
    response = client.get("/tin/validate?countryCode=AT&tinNumber=931736580")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == False