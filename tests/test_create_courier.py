
from data import  Courier
import allure 
from helpers import generate_courier_data,create_courier_request,login_courier_request,delete_courier_request
from data import Courier

class TestCourier:
    @allure.title("Создание курьера")
    def test_create_courier(self ):
        data = generate_courier_data()
        response = create_courier_request(data)
        
        assert response.status_code == 201
        assert response.json() == {"ok": True}
        login_data = {
            "login": data["login"],
            "password": data["password"]}
        login_response = login_courier_request(login_data)

        if login_response.status_code == 200:
            courier_id = login_response.json()["id"]
            delete_courier_request(courier_id)
    
    @allure.title("Создание дубликата курьера")
    @allure.step("Повторная отправка запроса с теми же данными.")
    def test_duplicate_courier(self): 
        data = generate_courier_data()
        create_courier_request(data)
        r = create_courier_request(data)
        
        assert r.status_code == 409
        assert "Этот логин уже используется" in r.text
    
    @allure.title("Ошибка при отсутствии пароля")
    def test_missing_password(self):
        r = create_courier_request(Courier.courier_without_password) 
        
        assert r.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in r.text
    
    @allure.title("Ошибка при отсутствии логина")
    def test_missing_login(self):
        r= create_courier_request(Courier.courier_without_login)
        
        assert r.status_code == 400
        assert "Недостаточно данных для создания учетной записи" in r.text

