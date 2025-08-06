from selenium.webdriver.common.by import By


class Locators:

    # Форма авторизации
    EMAIL = (By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @name="name"]')
    PASS = (By.XPATH, './/input[@class="text input__textfield text_type_main-default" and @name="Пароль"]')
    SHOW_PASS = (By.XPATH, './/div[contains(@class,"icon-action")]')
    VISIBLE_PASS = (By.XPATH, './/div/input[@class="text input__textfield text_type_main-default" and @type="text"]')
    LOGIN_BTN = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Войти"]')

    # Восстановление пароля
    RESTORE_LINK = (By.XPATH, './/a[@class="Auth_link__1fOlj" and text()="Восстановить пароль"]')
    RESTORE_BTN = (By.XPATH, './/button[@class="button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa" and text()="Восстановить"]')
    CODE_LABEL = (By.XPATH, './/div[@class="input pr-6 pl-6 input_type_text input_size_default"]/label[@class="input__placeholder text noselect text_type_main-default"]')
    RESTORE_TITLE = (By.XPATH, './/div[@class="Auth_login__3hAey"]/h2')

    # Личный кабинет
    PROFILE_LINK = (By.XPATH, './/a[@href="/account/profile"]')
    ORDERS_LINK = (By.XPATH, './/a[@href="/account/order-history"]')
    LOGOUT_BTN = (By.XPATH, './/button[text()="Выход"]')
    LAST_ORDER_NUM = (By.XPATH, './/ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]/li[last()]/a/div/p[@class="text text_type_digits-default"]')

    # Основная навигация
    ACCOUNT_BTN = (By.XPATH, './/*[text()="Личный Кабинет"]')
    CONSTRUCTOR_TAB = (By.XPATH, './/p[text()="Конструктор"]')
    FEED_TAB = (By.XPATH, './/p[@class="AppHeader_header__linkText__3q_va ml-2" and text()="Лента Заказов"]')

    # Конструктор бургеров
    BURGER_TITLE = (By.XPATH, './/h1[@class="text text_type_main-large mb-5 mt-10"]')
    BASCET = (By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]')
    BUN = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa6d"]')
    SAUCE = (By.XPATH, './/a[@href="/ingredient/61c0c5a71d1f82001bdaaa73"]')
    ORDER_BTN = (By.XPATH, './/button[text()="Оформить заказ"]')

    # Модальные окна
    ING_MODAL_TITLE = (By.XPATH, './/h2[@class="Modal_modal__title_modified__3Hjkd Modal_modal__title__2L34m text text_type_main-large pl-10"]')
    ING_MODAL_CLOSE = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    ORDER_MODAL_CLOSE = (By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]')
    ORDER_NUM = (By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')

    # Лента заказов
    FEED_TITLE = (By.XPATH, './/h1[@class="text text_type_main-large mt-10 mb-5"]')
    ORDER_CARD = (By.XPATH, './/li[@class="OrderHistory_listItem__2x95r mb-6"]')
    ORDER_MODAL = (By.XPATH, './/div[@class="Modal_orderBox__1xWdi Modal_modal__contentBox__sCy8X p-10"]')
    TOTAL_ORDERS = (By.XPATH, './/div[@class="undefined mb-15"]/p[2]')
    TODAY_ORDERS = (By.XPATH, './/div[@class="OrderFeed_ordersData__1L6Iv"]/div[3]/p[2]')
    IN_PROGRESS = (By.XPATH, './/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li[@class="text text_type_digits-default mb-2"]')
    