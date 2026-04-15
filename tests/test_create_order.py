import pytest 
import requests
from data import Url
import allure 
class CreateOrder():
    @allure.title("Создание заказа с разными цветами ")
    @pytest.mark.parametrize("colors", [ 
    ["BLACK"],
    ["GRAY"],
    ["BLACK","GRAY"],
    [] ])
    
    @allure.step("Отправка запроса на создание заказа")
    def test_create_order(self,colors):
        data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": colors
}
    
        response = requests.post(f'{Url.Base_url}{Url.Create_order}',json=data )
        assert response.status_code == 200
        assert 'track' in response.json()
