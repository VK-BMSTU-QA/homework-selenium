import pytest
from _pytest.fixtures import FixtureRequest
from ui.components.base_component import BaseComponent
from _pytest.fixtures import FixtureRequest
from ui.paths import paths
import time


class BaseCase:
    full_address = "Москва, Кравченко Улица, 22"

    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = BaseComponent(driver, url_config)

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, set_page):
        self.page.open()

    @pytest.fixture(scope="function")
    def authorize(self, request: FixtureRequest):
        self.driver.delete_all_cookies()
        cookies = request.getfixturevalue("cookies")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()

    @pytest.fixture(scope="function")
    def open(self):
        self.page.open()

    @pytest.fixture(scope="function")
    def set_address(self):
        self.driver.execute_script(f"window.localStorage.setItem('address','{self.full_address}');")

    @pytest.fixture(scope="function")
    def fill_cart(self, set_address):
        self.page.open_path(paths.GUAVA_DISHES)
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.wait_visability_of_elem(self.page.locators.CART)
        self.page.open()

    @pytest.fixture(scope="function")
    def order(self, set_address):
        self.page.open_path(paths.GUAVA_DISHES)
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.ORDER_BUTTON)
        self.page.click(self.page.locators.PAY_BUTTON)
        self.page.wait_visability_of_elem(self.page.locators.ORDER_HISTORY_HEADER)
        self.page.open()

    @pytest.fixture(scope="function")
    def order_go_to_review(self, set_address):
        self.page.open_path(paths.GUAVA_DISHES)
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.ORDER_BUTTON)
        self.page.click(self.page.locators.PAY_BUTTON)

        self.page.click(self.page.locators.DETAILS_BUTTON)

        time.sleep(10) # чтобы тест оставления отзыва прошел, нужно руками нажать на кнопку "оставить отзыв" в течении этих 10 секунд. Кнопка будет видна на экране
        # self.page.click(self.page.locators.SEND_REVIEW_BUTTON)
        # self.page.wait_visability_of_elem(self.page.locators.SEND_REVIEWS_HEADER)
