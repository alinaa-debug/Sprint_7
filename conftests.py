import pytest
import requests
from data import Url,generate_random_string

@pytest.fixture
def courier_data():
    return {
        "login": generate_random_string(10),
        "password": generate_random_string(10),
        "firstName": generate_random_string(10)
    }
   

@pytest.fixture
def create_courier(courier_data):
    
    requests.post(f'{Url.Base_url}{Url.Create_url}',data=courier_data)

    yield courier_data
    
    login_data ={'login':courier_data['login'],
                  'password': courier_data['password']}

    login_response =requests.post(f'{Url.Base_url}{Url.Login_url}',data= login_data)
    if login_response.status_code == 200:
        courier_id = login_response.json()['id']
    requests.delete(f'{Url.Base_url}{Url.Create_url}/{courier_id}')

    