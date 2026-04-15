import requests
from data import Url
import allure
class LoginCourier:
    @allure.title('Создание курьера')
    def test_login_courier(self, login_courier):      
        response = login_courier
        assert  response.status_code == 200
        assert  'id' in response.json()
    
    @allure.title("Логин без пароля")
    def test_missing_in_login_password(self, create_courier):
        
        login_data = {
            "login": create_courier["login"]
        }
        response = requests.post(
            f'{Url.Base_url}{Url.Login_url}',
            data=login_data)
        assert response.status_code == 400
        assert 'Недостаточно данных для входа' in  response.text


    @allure.title("Логин с неправильным логином")
    def test_wrong_login(self, create_courier):
    
        login_data = {"login":'wrong_login',
                      "password": create_courier['password']}
        response = requests.post(f'{Url.Base_url}{Url.Login_url}',data = login_data)
        assert response.status_code == 404
        assert 'Учетная запись не найдена' in  response.text
    
    @allure.title("Логин с неправильным паролем")
    def test_wrong_password(self,create_courier):
    
        login_data = {"login": create_courier['login'],
                      "password": 'wrong_password'}
        response = requests.post(f'{Url.Base_url}{Url.Login_url}',data = login_data)
        assert response.status_code == 404
        assert 'Учетная запись не найдена' in  response.text