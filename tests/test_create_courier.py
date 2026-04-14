import requests
from data import Url

class TestCourier:
    def test_create_courier(self,create_courier ):
        payload, response = create_courier
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    def test_duplicate_courier(self, create_courier):
        payload ,_= create_courier 
        
        r= requests.post(f'{Url.Base_url}{Url.Create_url}',data = payload)
        assert r.status_code == 409
        assert "используется" in r.text

    def test_missing_password(self):
        payload = {
    "login": "ninja",
    "firstName": "saske"}    
        r = requests.post(f'{Url.Base_url}{Url.Create_url}',data = payload)
        assert r.status_code == 400
        assert "Недостаточно данных " in r.text

    def test_missing_login(self):
        payload = {
    "password": "1234",
    "firstName": "saske"    }
        r = requests.post(f'{Url.Base_url}{Url.Create_url}',data = payload)

        assert r.status_code == 400
        assert "Недостаточно данных " in r.text

