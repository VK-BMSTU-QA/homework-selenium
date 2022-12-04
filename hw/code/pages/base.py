from typing import List, Union
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver: WebDriver, add_url: Union[str, None] = None) -> None:
        self.driver = driver
        self.base_url = "http://overmail.online/"
        self.add_url = add_url

    def find_element(self, locator, time=2, soft: bool = False) -> Union[WebElement, None]:
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                          message=f"Can't find element by locator {locator}")
        except TimeoutException:
            if soft:
                return None
            raise

    def find_elements(self, locator, time=2, soft: bool = False) -> List[WebElement]:
        try:
            return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                          message=f"Can't find elements by locator {locator}")
        except TimeoutException:
            if soft:
                return []
            raise

    def go_to_site(self) -> None:
        url = self.base_url + self.add_url if self.add_url else self.base_url
        return self.driver.get(url)

    def is_url_endswith(self, part: str, time=10) -> bool:
        WebDriverWait(self.driver, time).until(EC.url_contains(part),
                                               message=f"Url {self.driver.current_url} doesn't contain {part}")
        return self.driver.current_url.endswith(part)

    def is_loaded(self) -> bool:
        '''Загружена ли страница'''
        raise NotImplementedError

    def is_redirected(self) -> bool:
        '''Была ли страница перенаправлена на другую страницу. Только для поддерживаемых страниц.'''
        raise NotImplementedError

    def is_elem(self, locator, time=2, soft: bool = False) -> bool:
        '''Есть ли элемент на странице и он видимый'''
        elem = self.find_element(locator, time=time, soft=soft)
        return bool(elem)

    def click(self, locator):
        elem = self.find_element(locator)
        assert elem
        elem.click()

    def get_css_property(self, locator, name) -> str:
        elem = self.find_element(locator, time=10)
        assert elem
        return elem.value_of_css_property(name)
