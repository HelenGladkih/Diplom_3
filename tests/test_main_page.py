import allure
import pytest
from locators import *
from data import Urls
from pages.main_page import MainPage
from pages.auth_page import AuthPage


@allure.feature("Главная страница")
class TestMainPage:

    @pytest.mark.parametrize('locator, check_locator, result_text', [
        (Locators.CONSTRUCTOR_TAB, Locators.BURGER_TITLE, "Соберите бургер"),
        (Locators.FEED_TAB, Locators.FEED_TITLE, "Лента заказов")
    ])
    @allure.title('Проверка навигации по разделам главной страницы')
    @allure.description('''
    Проверка корректности перехода между разделами:
    * При клике на кнопку навигации должен происходить переход в соответствующий раздел
    * Должен отображаться корректный заголовок раздела
    ''')
    def test_main_page_navigation(self, main_page, locator, check_locator, result_text):
        main_page.click(locator)
        result = main_page.wait_element(check_locator)
        assert result.text == result_text, f"Ожидался текст '{result_text}', получено: '{result.text}'"


    @pytest.mark.parametrize('ingredient_locator, count_expect', [(Locators.BUN, '2'), (Locators.SAUCE, '1')])
    @allure.title('Проверка счетчика ингредиентов при добавлении')
    @allure.description('''
    Проверка работы счетчика добавленных ингредиентов:
    * При добавлении ингредиента в конструктор должен увеличиваться соответствующий счетчик
    * Счетчик должен отображать корректное количество добавленных ингредиентов
    ''')
    def test_ingredient_counter(self, main_page, ingredient_locator, count_expect):
        count_fact = main_page.add_ingredient(ingredient_locator)
        assert count_fact == count_expect, f"Ожидалось значение '{count_expect}', получено: '{count_fact}'"


    @allure.title('Проверка отображения деталей ингредиента в модальном окне')
    @allure.description('''
    Проверка работы модального окна:
    * При клике на ингредиент должно открываться модальное окно с деталями
    * Окно должно содержать корректный заголовок
    ''')
    def test_ingredient_details_modal(self, main_page):
        ingredient_window = main_page.open_ingredient_details()
        assert ingredient_window.text == "Детали ингредиента", "Не отображается окно с деталями ингредиента"


    @allure.title('Проверка закрытия модального окна')
    @allure.description('''
    Проверка функционала закрытия модального окна:
    * При клике на кнопку закрытия модальное окно должно скрываться
    * После закрытия окно не должно отображаться на странице
    ''')
    def test_close_modal_window(self, main_page):
        modal_window = main_page.open_ingredient_details()
        main_page.close_details()
        assert modal_window.is_displayed() is False, "Модальное окно осталось видимым после закрытия"


    @allure.title('Проверка оформления заказа авторизованным пользователем')
    @allure.description('''
    Проверка полного цикла оформления заказа:
    * Авторизованный пользователь должен иметь возможность оформить заказ
    * После оформления должен отображаться номер заказа
    * Номер заказа должен быть валидным (отличаться от тестового значения)
    ''')
    def test_authorized_user_order(self, driver, new_user):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.go_to_account()
        auth_page = AuthPage(driver)
        auth_page.authorization(new_user[0])
        order_number = main_page.make_order()
        assert order_number != '9999', "Не удалось оформить заказ (получен тестовый номер)"
