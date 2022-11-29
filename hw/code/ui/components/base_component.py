import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from contextlib import contextmanager
import urllib.parse as urlparse
from ui.locators import locators


class PageNotOpenedExeption(Exception):
    pass


class StaleTimeoutExeption(Exception):
    pass


class BaseComponent(object):
    default_timeout = 15
    mini_timeout = 3
    locators = locators.BasePageLocators()
    PATH = ""

    def is_opened(self, url, timeout=default_timeout):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == url:
                return True
        raise PageNotOpenedExeption(f"{url} did not open in {timeout} sec, current url {self.driver.current_url}")

    def __init__(self, driver, url):
        self.driver = driver
        self.action = ActionChains(driver)
        self.BASE_URL = url

    def open(self, timeout=default_timeout):
        url = urlparse.urljoin(self.BASE_URL, self.PATH)
        self.driver.get(url)
        self.driver.maximize_window()
        self.is_opened(url, timeout)

    def open_path(self, path, timeout=default_timeout):
        url = urlparse.urljoin(self.BASE_URL, path)
        self.driver.get(url)
        self.driver.maximize_window()
        self.is_opened(url, timeout)

    def wait(self, timeout=default_timeout):
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    def wait_visability_of_elem(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.visibility_of_element_located(locator))

    def is_visible(self, locator, timeout=mini_timeout):
        try:
            self.wait(timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_invisible(self, locator, timeout=mini_timeout):
        try:
            self.wait(timeout).until(EC.invisibility_of_element_located(locator))
        except TimeoutException:
            return False
        return True

    def is_url(self, path):
        return EC.url_matches(urlparse.urljoin(self.BASE_URL, path))

    def is_active(self, elem):
        return self.driver.switch_to.active_element == elem

    def has_value(self, elem, value):
        return elem.get_attribute("value") == value

    def find_all_elems(self, locator, timeout=default_timeout):
        return self.wait(timeout).until(EC.presence_of_all_elements_located(locator))

    def send_keys(self, locator, keys, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.find(locator, timeout - (time.time() - started))
                elem.clear()
                elem.send_keys(keys)
                return elem
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutExeption(f"{locator} did not clickable or hav been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")

    def send_keys_enter(self, locator, keys, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.find(locator, timeout - (time.time() - started))
                elem.clear()
                elem.send_keys(keys)
                elem.send_keys(Keys.RETURN)
                return elem
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutExeption(f"{locator} did not clickable or hav been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")


    def click(self, locator, timeout=default_timeout) -> WebElement:
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.wait(timeout - (time.time() - started)).until(EC.element_to_be_clickable(locator))
                elem.click()
                return elem
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutExeption(f"{locator} did not clickable or hav been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")

    @contextmanager
    def wait_for_reload_elem(self, locator, timeout=default_timeout):
        old_elem = self.find(locator)
        yield
        WebDriverWait(self.driver, timeout).until(EC.staleness_of(old_elem))

    def click_after(self, locator, dy, timeout=default_timeout):
        started = time.time()
        while time.time() - started < timeout:
            try:
                elem = self.wait(timeout - (time.time() - started)).until(EC.element_to_be_clickable(locator))
                elem.click()
                self.action.move_to_element_with_offset(elem, 0, elem.size["height"] + dy).click().perform()
                return elem
            except StaleElementReferenceException as Exception:
                pass
        raise StaleTimeoutExeption(f"{locator} did not clickable or hav been throwing StaleElementReferenceExceptions in {timeout} sec, current url {self.driver.current_url}")
