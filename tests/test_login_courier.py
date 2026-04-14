import requests
from data import Url

class LoginCourier:
    
    def test_login_courier(self, login_courier):      
        response = login_courier
        assert  response.status_code == 200
        assert  'id' in response.json()
    
    def test_missing_in_login_password(self, create_courier):
        payload, _ = create_courier

        login_data = {
            "login": payload["login"]
        }
        response = requests.post(
            f'{Url.Base_url}{Url.Login_url}',
            data=login_data)
        assert response.status_code == 400
        assert 'Недостаточно' in  response.text



    def test_wrong_login(self, create_courier):
        payload ,_ = create_courier
        login_data = {"login":'wrong_login',
                      "password": payload['password']}
        response = requests.post(f'{Url.Base_url}{Url.Login_url}',data = login_data)
        assert response.status_code == 404
        assert 'не найдена' in  response.text

    def test_wrong_password(self,create_courier):
        payload ,_ = create_courier
        login_data = {"login": payload['login'],
                      "password": 'wrong_password'}
    
        response = requests.post(f'{Url.Base_url}{Url.Login_url}',data = login_data)
        assert response.status_code == 404
        assert 'не найдена' in  response.text