import allure 
from helpers import get_orders_request

class OrderList:
    @allure.title("Получение списка заказов")
    
    def test_order_list(self):
        response = get_orders_request()
        assert response.status_code == 200
        assert  "pageInfo" in response.json()