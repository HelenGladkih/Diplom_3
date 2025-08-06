import pytest
from helpers import *
from selenium import webdriver
from pages.main_page import MainPage
from pages.auth_page import AuthPage
from pages.feed_page import FeedPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=chrome_options)
    else:
        driver = webdriver.Firefox()

    yield driver
    driver.quit()

@pytest.fixture
def new_user():
    """
    Фикстура создаёт нового пользователя.
    После завершения теста удаляет пользователя.
    """
    result = User.register_user()
    accessToken = result[1].json().get('accessToken')
    yield result
    User.delete_user(accessToken)

@pytest.fixture
def main_page(driver):
    """
    Фикстура создаёт и возвращает экземпляр главной страницы.
    Перед тестом открывает главную страницу.
    """
    page = MainPage(driver)
    page.driver.get(Urls.MAIN_PAGE)
    return page

@pytest.fixture
def feed_page(driver):
    """
    Фикстура создаёт и возвращает экземпляр страницы ленты заказов.
    Перед тестом открывает страницу ленты заказов.
    """
    feed_page = FeedPage(driver)
    feed_page.driver.get(Urls.FEED_PAGE)
    return feed_page

@pytest.fixture
def auth_page(driver):
    """
    Фикстура создаёт и возвращает экземпляр страницы авторизации.
    Перед тестом открывает страницу авторизации.
    """
    auth_page = AuthPage(driver)
    auth_page.driver.get(Urls.AUTH_PAGE)
    return auth_page
