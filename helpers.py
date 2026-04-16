import requests
import random
import string
import allure
from data import Url


def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))



def generate_courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }


@allure.step("Создание курьера")
def create_courier_request(data):
    return requests.post(
        f'{Url.Base_url}{Url.Create_url}',
        data=data
    )


@allure.step("Логин курьера")
def login_courier_request(data):
    return requests.post(
        f'{Url.Base_url}{Url.Login_url}',
        data=data
    )


@allure.step("Удаление курьера")
def delete_courier_request(courier_id):
    return requests.delete(
        f'{Url.Base_url}{Url.Create_url}/{courier_id}'
    )



@allure.step("Создание заказа")
def create_order_request(data):
    return requests.post(
        f"{Url.Base_url}{Url.Create_order}",
        json=data )



@allure.step("Получение заказов")
def get_orders_request():
    return requests.get(
 f"{Url.Base_url}{Url.Create_order}")


def build_login_data(data):
    login_data ={'login':data['login'],
                  'password': data['password']}