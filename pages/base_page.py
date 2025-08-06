import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:

    @allure.step('Получить и инициализировать драйвер')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Получить элемент с ожиданием')
    def wait_element(self, locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Ожидать кликабельности, клик по элементу')
    def click(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        browser = self.driver.name.lower()
        if browser == 'firefox':
            self.click_ff(locator)
        else:
            self.driver.find_element(*locator).click()

    @allure.step('Клик по элементу')
    def click_modal(self, locator):
        WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(locator))
        browser = self.driver.name.lower()
        if browser == 'firefox':
            self.scroll_click(locator)
        else:
            self.driver.find_element(*locator).click()

    @allure.step('Получить текст элемента')
    def get_text(self, locator):
        return self.wait_element(locator).text

    @allure.step('Прокрутить страницу до элемента')
    def scroll_to(self, locator):
        element = self.wait_element(locator)
        try:
            ActionChains(self.driver).move_to_element(element).perform()
        except:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Прокрутить до элемента и кликнуть')
    def scroll_click(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(locator))
        self.scroll_to(locator)
        try:
            element.click()
        except:
            self.driver.execute_script("arguments[0].click();", element)
            
    @allure.step('Заполнить поле данными')
    def fill(self, locator, text):
        self.wait_element(locator).send_keys(text)

    @allure.step('Клик на элемент, закрытый модальным окном')
    def click_ff(self, locator):
        element = self.driver.find_element(*locator)
        ActionChains(self.driver).move_to_element(element).click().perform()

    @allure.step('Перетащить объект для Chrome')
    def drag_drop_chrome(self, from_locator, to_locator):
        element_from = self.wait_element(from_locator)
        element_to = self.wait_element(to_locator)
        actions = ActionChains(self.driver)
        actions.drag_and_drop(element_from, element_to).perform()

    @allure.step('Перетащить объект для Firefox')
    def drag_drop_ff(self, locator_from, locator_to):
        self.wait_element(locator_from)
        self.wait_element(locator_to)
        element_from = self.driver.find_element(*locator_from)
        element_to = self.driver.find_element(*locator_to)
        self.driver.execute_script("""
                   var source = arguments[0];
                   var target = arguments[1];
                   var evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   target.dispatchEvent(evt);
                   evt = document.createEvent("DragEvent");
                   evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
                   source.dispatchEvent(evt);
               """, element_from, element_to)

    @allure.step('Перетащить объект (Chrome или Firefox)') 
    def drag_drop(self, locator_from, locator_to):
        browser = self.driver.name.lower()
        if browser == 'firefox':
            self.drag_drop_ff(locator_from, locator_to)
        else:
            self.drag_drop_chrome(locator_from, locator_to)

    @allure.step('Ожидать изменения текста')
    def wait_text_change(self, locator, initial_text):
        def predicate(driver):
            try:
                current = driver.find_element(*locator).text
                return current != initial_text
            except:
                return False
        return predicate 

    @allure.step('Ожидать скрытия элемента')
    def wait_hide(self, locator):
        WebDriverWait(self.driver, 50).until(EC.invisibility_of_element(locator))

    @allure.step('Ожидать появления текста')
    def wait_text(self, locator, text):
        WebDriverWait(self.driver, 50).until(self.wait_text_change(locator, text))
