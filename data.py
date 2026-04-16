
class Url:
    Base_url = 'https://qa-scooter.praktikum-services.ru'
    Create_url = '/api/v1/courier'
    Login_url = '/api/v1/courier/login'
    Create_order = '/api/v1/orders'
    

class Courier:
    courier_without_password = {
    "login": "ninja",
    "firstName": "saske"
}

    courier_without_login = {
    "password": "1234",
    "firstName": "saske"
} 
    
class OrderData:
    base_data = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": 4,
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha"}

