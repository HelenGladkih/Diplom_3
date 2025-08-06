import allure 
from data import *
from pages.auth_page import AuthPage
from pages.main_page import MainPage


@allure.feature("Личный кабинет пользователя")
class TestUserProfile:

    @allure.title('Проверка доступа к профилю после авторизации')
    @allure.description('''
    Проверка корректности перехода в личный кабинет:
    * Авторизованный пользователь должен иметь доступ к разделу "Профиль"
    * При переходе в личный кабинет должен отображаться корректный заголовок раздела
    ''')
    def test_profile_access_after_login(self, driver, new_user):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.go_to_account()
        auth_page = AuthPage(driver)
        auth_page.authorization(new_user[0])
        main_page.go_to_account()
        assert auth_page.get_profile_title() == "Профиль", (
            f"Не отображается раздел 'Профиль', но получено: {auth_page.get_profile_title()}"
        )    


    @allure.title('Проверка доступа к истории заказов')
    @allure.description('''
    Проверка корректности работы раздела истории заказов:
    * Авторизованный пользователь должен иметь доступ к истории заказов
    * Раздел "История заказов" должен корректно активироваться при переходе
    ''')
    def test_order_history_access(self, driver, new_user):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.go_to_account()
        auth_page = AuthPage(driver)
        auth_page.authorization(new_user[0])
        main_page.go_to_account()
        assert auth_page.is_history_active(), "Раздел 'История заказов' не активен"


    @allure.title('Проверка выхода из учетной записи')
    @allure.description('''
    Проверка корректности выхода из системы:
    * После нажатия кнопки "Выход" пользователь должен быть перенаправлен на страницу авторизации
    * Должен отображаться корректный заголовок страницы авторизации
    ''')
    def test_user_logout(self, driver, new_user):
        driver.get(Urls.MAIN_PAGE)
        main_page = MainPage(driver)
        main_page.go_to_account()
        auth_page = AuthPage(driver)
        auth_page.authorization(new_user[0])
        main_page.go_to_account()
        logout = auth_page.logout()
        assert logout == "Вход", "Не произошел переход на страницу авторизации"
