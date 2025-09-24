import allure
from pages.base_page import BasePage
from data import *
from locators import *
from helpers import *


class FeedPage(BasePage):

    @allure.step('Открыть детали заказа в ленте')
    def open_order(self):
        self.click(Locators.ORDER_CARD)
        return self.wait_element(Locators.ORDER_MODAL)

    @allure.step('Найти заказ в ленте по номеру')
    def find_order(self, number):
        locator = get_order_number_locator(number)
        return self.wait_element(locator)
