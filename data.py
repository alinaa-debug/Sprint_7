import random
import string

class Url:
    Base_url = 'https://qa-scooter.praktikum-services.ru'
    Create_url = '/api/v1/courier'
    Login_url = '/api/v1/courier/login'
    Create_order = '/api/v1/orders'
    

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))  

    