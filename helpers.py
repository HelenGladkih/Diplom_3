import requests
import allure
import random
import string
from data import *
from selenium.webdriver.common.by import By


@allure.step('Сгенерировать новые рег.данных')
def generate_user_data():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string
    email = f"test_{generate_random_string(10)}@yandex.ru"
    password = generate_random_string(10)
    name = f"User_{generate_random_string(10)}"
    payload = {
        "email": email,
        "password": password,
        "name": name
    }
    return payload

class User:
    @staticmethod
    @allure.step('Регистрация пользователя через API')
    def register_user():
        payload = generate_user_data()
        response = requests.post(Urls.API_REG_USER, data=payload)
        auth_data = []
        if response.status_code == 200:
            auth_data = payload
        return auth_data, response   

    @staticmethod
    @allure.step('Удаление УЗ пользователя через API')
    def delete_user(auth_token):
        delete = requests.delete(Urls.API_DELETE_USER, headers={'Authorization': auth_token})
        return delete


def get_ingredient_counter_locator(locator):
    """
    Формирует локатор для счётчика ингредиента на основе переданного базового локатора.
    Возвращает обновлённый локатор, указывающий на текстовый элемент с количеством.
    """
    xpath = locator[1]
    formatted_xpath = f'{xpath}/div/p'
    return (By.XPATH, formatted_xpath)

def get_order_number_locator(number):
    """
    Формирует XPath-локатор для поиска номера заказа в интерфейсе.
    Возвращает локатор, который ищет элемент с текстом, равным переданному номеру.
    """
    format_number = f'.//p[text()="{number}"]'
    locator = (By.XPATH, format_number)
    return locator
