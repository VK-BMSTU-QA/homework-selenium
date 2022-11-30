import pytest
from ui.components.recommendations_elemet import RecommendationsElement
from ui.base_case.base_case import BaseCase


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = RecommendationsElement(driver, url_config)

    def test_recommendations_exist(self, authorize, set_address):
        self.page.add_to_cart()
        assert self.page.is_visible(self.page.locators.RECOMMENDATIONS)

    def test_add_recommendations_dish(self, authorize, set_address):
        self.page.add_to_cart()
        self.page.add_recommendation()
        assert self.page.is_visible(self.page.locators.RECOMMENDATION_DISH_IN_CART)
