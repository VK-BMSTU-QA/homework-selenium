import pytest
from ui.paths import paths
from selenium.webdriver.support import expected_conditions as EC
from ui.components.recommendations_elemet import RecommendationsElement
from ui.locators import locators
from ui.base_case.base_case import BaseCase
from _pytest.fixtures import FixtureRequest
import time


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = RecommendationsElement(driver, url_config)

    def test_recommendations_exist(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        assert self.page.is_visible(self.page.locators.RECOMMENDATIONS)

    def test_add_recommendations_dish(self, authorize, set_address):
        self.page.click(self.page.locators.ADD_TO_CART_BUTTON)
        self.page.click(self.page.locators.ADD_RECOMMENDATIONS)
        assert self.page.is_visible(self.page.locators.RECOMMENDATION_DISH_IN_CARD)
