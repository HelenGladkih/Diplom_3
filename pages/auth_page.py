import allure
from pages.base_page import BasePage
from data import *
from locators import *


class AuthPage(BasePage):

    @allure.step("Открыть страницу авторизации")
    def open_page(self):
        self.driver.get(Urls.AUTH_PAGE)

    @allure.step('Клик по "Восстановить пароль"')
    def go_to_restore(self):
        self.wait_element(Locators.RESTORE_LINK)
        self.click(Locators.RESTORE_LINK)
        self.wait_element(Locators.EMAIL)
        title_element = self.get_text(Locators.RESTORE_TITLE)
        return title_element

    @allure.step('Восстановить пароль')
    def restore_pass(self, email):
        self.go_to_restore()
        self.fill(Locators.EMAIL, email)
        self.click(Locators.RESTORE_BTN)
        restore_code_text = self.get_text(Locators.CODE_LABEL)
        return restore_code_text

    @allure.step('Проверить заголовок страницы авторизации')
    def get_auth_title(self):
        return self.get_text(Locators.RESTORE_TITLE)

    @allure.step('Проверить заголовок раздела профиля')
    def get_profile_title(self):
        return self.get_text(Locators.PROFILE_LINK)

    @allure.step('Авторизоваться')
    def authorization(self, user_data):
        email, password = user_data.get('email'), user_data.get('password')
        self.fill(Locators.EMAIL, email)
        self.fill(Locators.PASS, password)
        self.click(Locators.LOGIN_BTN)

    @allure.step('Проверить видимость поля пароля')
    def is_pass_visible(self):
        self.wait_element(Locators.PASS)
        self.click_ff(Locators.SHOW_PASS)
        return bool(self.wait_element(Locators.VISIBLE_PASS))

    @allure.step('Проверить активность вкладки истории заказов')
    def is_history_active(self):
        self.click(Locators.ORDERS_LINK)
        element = self.wait_element(Locators.ORDERS_LINK)
        return element.get_attribute("class") == ACTIVE_ORDER_HISTORY_TAB_CLASSES

    @allure.step('Выйти из аккаунта')
    def logout(self):
        self.click(Locators.LOGOUT_BTN)
        return self.get_auth_title()

    @allure.step('Получить номер последнего заказа из истории')
    def get_last_order(self):
        return self.get_text(Locators.LAST_ORDER_NUM)
