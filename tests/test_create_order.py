import pytest 
from helpers import create_order_request
from data import OrderData

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
        data = OrderData.base_data.copy()
        data['color']= colors
    
        response = create_order_request(data)
        assert response.status_code == 200
        assert 'track' in response.json()
