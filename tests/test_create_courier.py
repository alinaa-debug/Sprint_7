import requests
from data import Url, Courier
import allure 

class TestCourier:
    @allure.title("Создание курьера")
    @allure.step("ОТправка запроса на создание курьера")
    def test_create_courier(self,courier_data ):
        response = requests.post(
            f'{Url.Base_url}{Url.Create_url}',data = courier_data
        )
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
    
    @allure.title("Создание дубликата курьера")
    @allure.step("Повторная отправка запроса с теми же данными.")
    def test_duplicate_courier(self, create_courier): 
        requests.post(
            f'{Url.Base_url}{Url.Create_url}',data = create_courier
        )
        r= requests.post(f'{Url.Base_url}{Url.Create_url}',data = create_courier)
        assert r.status_code == 409
        assert "Этот логин уже используется" in r.text
    
    @allure.title("Ошибка при отсутствии пароля")
    def test_missing_password(self):
          
        r = requests.post(f'{Url.Base_url}{Url.Create_url}',data = Courier.courier_without_password )
        assert r.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in r.text
    
    @allure.title("Ошибка при отсутствии логина")
    def test_missing_login(self):
        
        r = requests.post(f'{Url.Base_url}{Url.Create_url}',data = Courier.courier_without_login)
        assert r.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in r.text

