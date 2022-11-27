import time

import allure
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver import ActionChains
from ui.locators import basic_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    locators = basic_locators.BasePageLocators()
    url = 'https://movie-space.ru/'

    def is_opened(self, url, timeout=15):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True
        raise PageNotOpenedExeption(
            f'{url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        # self.is_opened(self.url)

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait_visability_of_elem(self, locator, timeout=None):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def find_all_elemets(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def send_keys(self, element, keys):
        element.clear()
        element.send_keys(keys)

    def move_on_element(self, locator, timeout=None) -> WebElement:
        hoverable = self.find(locator)
        ActionChains(self.driver)\
            .move_to_element(hoverable)\
            .perform()

    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

    def elem_click(self, elem, timeout=None) -> WebElement:
        self.wait(timeout).until(EC.element_to_be_clickable(elem))
        elem.click()