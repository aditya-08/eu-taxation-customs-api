from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_get_1():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=A234567890")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_2():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1A34567890")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_3():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12A4567890")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_4():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=123A567890")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_5():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1234A67890")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_6():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12345A7890")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_7():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=123456A890")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1234567A90")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12345678A0")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_10():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=123456789A")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_1():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=123456789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_2():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1A3456789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_3():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12A456789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_4():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=123A56789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_5():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1234A6789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_6():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12345A789")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_7():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=123456A89")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_8():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1234567A9")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_9_9():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12345678A")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8_1():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12345678")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8_2():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1A345678")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8_3():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12A45678")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8_4():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=123A5678")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8_5():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1234A678")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8_6():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=12345A78")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8_7():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=123456A8")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_8_8():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=1234567A")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_0_D():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=DA345678")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False

def test_get_0_D():
    response = client.get("/tin/validate?countryCode=UK&tinNumber=AD345678")
    assert response.status_code == 200
    assert response.json()["validStructure"] == False