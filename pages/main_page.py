import allure
from pages.base_page import BasePage
from locators import *
from helpers import *


class MainPage(BasePage):

    @allure.step('Клик по "Личный кабинет"')
    def go_to_account(self):
        self.click_modal(Locators.ACCOUNT_BTN)

    @allure.step('Клик по "Лента заказов"')
    def go_to_feed(self):
        self.click_modal(Locators.FEED_TAB)

    @allure.step('Клик по "Конструктор"')
    def go_to_constructo(self):
        self.click(Locators.CONSTRUCTOR_TAB)

    @allure.step('Добавить ингредиент в корзину')
    def add_ingredient(self, ingredient_locator):
        self.drag_drop(ingredient_locator, Locators.BASCET)
        counter_locator = get_ingredient_counter_locator(ingredient_locator)
        counter = self.wait_element(counter_locator)
        return counter.text

    @allure.step('Собрать бургер и оформить заказ')
    def make_order(self):
        self.drag_drop(Locators.BUN, Locators.BASCET)
        self.drag_drop(Locators.SAUCE, Locators.BASCET)
        self.click(Locators.ORDER_BTN)
        self.wait_element(Locators.ORDER_NUM)
        self.wait_text(Locators.ORDER_NUM, '9999')
        return self.get_text(Locators.ORDER_NUM)

    @allure.step('Открыть детали ингредиента')
    def open_ingredient_details(self):   
        self.click(Locators.BUN)
        return self.wait_element(Locators.ING_MODAL_TITLE)

    @allure.step('Закрыть модальное окно с деталями ингредиента')
    def close_details(self):
        self.click(Locators.ING_MODAL_CLOSE)
        self.wait_hide(Locators.ING_MODAL_CLOSE)

    @allure.step('Закрыть модальное окно с деталями заказа')
    def close_order(self):
        self.click(Locators.ORDER_MODAL_CLOSE)
