import pytest 
from helpers import (generate_courier_data, 
                     create_courier_request,
                     login_courier_request,
                     delete_courier_request,
                     build_login_data)


@pytest.fixture
def create_courier():
    data = generate_courier_data()
    create_courier_request(data)

    yield data
    
    login_data = build_login_data(data)

    login_response = login_courier_request(login_data)
    if login_response.status_code == 200:
        courier_id = login_response.json()['id']
        delete_courier_request(courier_id)

    