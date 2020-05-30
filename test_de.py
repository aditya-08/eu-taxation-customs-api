from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_1():
    response = client.get("/tin/validate?countryCode=DE&tinNumber=26954371827")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_2():
    response = client.get("/tin/validate?countryCode=DE&tinNumber=86095742719")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_3():
    response = client.get("/tin/validate?countryCode=DE&tinNumber=65929970489")
    assert response.status_code == 200
    assert response.json()["validStructure"] == True
    assert response.json()["validSyntax"] == True

def test_get_4():
    response = client.get("/tin/validate?countryCode=DE&tinNumber=579461005")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False
    assert response.json()["validSyntax"] == False
    