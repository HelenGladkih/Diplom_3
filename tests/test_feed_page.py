import allure
import pytest
from locators import *
from pages.main_page import MainPage
from pages.feed_page import FeedPage
from pages.auth_page import AuthPage


@allure.feature("Лента заказов")
class TestFeedPage:

    @allure.title('Проверка отображения деталей заказа')
    @allure.description('''
    Проверка работы модального окна с деталями заказа:
    * При клике на заказ должно открываться модальное окно с информацией
    * Окно с деталями заказа должно быть видимым на странице
    ''')
    def test_order_details_display(self, feed_page):
        info_window = feed_page.open_order()
        assert info_window.is_displayed() is True, "Окно с информацией о заказе не отображается"


    @allure.title('Проверка синхронизации истории заказов и ленты заказов')
    @allure.description('''
    Проверка корректности отображения заказов:
    * Заказ, созданный пользователем, должен отображаться в его истории заказов
    * Этот же заказ должен быть виден в общей ленте заказов
    * Номера заказов должны совпадать в обоих разделах
    ''')
    def test_order_number_matching(self, driver, new_user):
        auth_page = AuthPage(driver)
        auth_page.open_page()
        auth_page.authorization(new_user[0])
        main_page = MainPage(driver)
        main_page.make_order()
        main_page.close_order()
        main_page.go_to_account()
        auth_page.is_history_active()
        number = auth_page.get_last_order()
        main_page.go_to_feed()  #click_on_queue_of_orders
        queue_page = FeedPage(driver)
        order_by_number = queue_page.find_order(number)
        assert order_by_number.is_displayed() is True, f"Заказ с номером {number} не найден в ленте заказов"


    @pytest.mark.parametrize('locator', [Locators.TOTAL_ORDERS, Locators.TODAY_ORDERS])
    @allure.title('Проверка обновления счетчиков заказов')
    @allure.description('''
    Проверка работы счетчиков заказов:
    * При создании нового заказа должен увеличиваться счетчик "Выполнено за все время"
    * При создании нового заказа должен увеличиваться счетчик "Выполнено за сегодня"
    * Увеличение счетчиков должно быть синхронным
    ''')
    def test_counters_increase(self, locator, driver, new_user):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        auth_page.open_page()
        auth_page.authorization(new_user[0])
        main_page.go_to_feed()
        counter = int(main_page.get_text(locator))
        main_page.go_to_constructo()
        main_page.make_order()
        main_page.close_order()
        main_page.go_to_feed()
        new_counter = int(main_page.get_text(locator))
        assert new_counter > counter, f"Счетчик не увеличился. Было: {counter}, стало: {new_counter}"


    @allure.title('Проверка статуса нового заказа')
    @allure.description('''
    Проверка корректности отображения статуса заказа:
    * Новый заказ должен отображаться в разделе "В работе"
    * Номер заказа должен соответствовать созданному заказу
    * Статус должен обновляться в реальном времени
    ''')
    def test_order_in_progress_status(self, driver, new_user):
        auth_page = AuthPage(driver)
        main_page = MainPage(driver)
        auth_page.open_page()
        auth_page.authorization(new_user[0])
        order_number = main_page.make_order()
        order_number = '0' + order_number
        main_page.close_order() #close_order_window
        main_page.go_to_feed()
        order_list = main_page.get_text(Locators.IN_PROGRESS)
        assert str(order_number) in str(order_list), f"Номер заказа {order_number} не находится в колонке: {order_list}"
