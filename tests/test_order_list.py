import requests
from data import Url
import allure 

class OrderList:

    @allure.title("Получение списка заказов")
    @allure.step("Отправка запроса на получение списка заказов")
    def test_order_list(self):
        response = requests.get(f'{Url.Base_url}{Url.Create_order}')
        assert response.status_code == 200
        assert  "pageInfo" in response.json()