import pytest
from ui.paths import paths
from ui.components.promo_codes_element import PromoCodesElement
from ui.base_case.base_case import BaseCase


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = PromoCodesElement(driver, url_config)

    def test_promo_code(self, authorize, set_address):
        self.page.click(self.page.locators.PROMO_CODE)
        assert self.page.is_visible(self.page.locators.PROMO_CODE_RESET)
        assert self.page.is_url_matches(paths.CART)
