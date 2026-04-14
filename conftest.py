import pytest
import requests
from data import Url,generate_random_string


@pytest.fixture
def create_courier():
    payload = {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }

    
    response = requests.post(
        f'{Url.Base_url}{Url.Create_url}',
        data=payload)
    return payload, response

@pytest.fixture
def login_courier(create_courier):
    payload, _ = create_courier
    login_data = {'login':payload['login'],
                  'password': payload['password']}
    response = requests.post(f'{Url.Base_url}{Url.Login_url}',data = login_data)

    return response 

