import pytest
from ui.paths import paths
from selenium.webdriver.support import expected_conditions as EC
from ui.components.comments_page import CommentsElement
from ui.locators import locators
from ui.base_case.base_case import BaseCase
from _pytest.fixtures import FixtureRequest
import time


class TestMenuPage(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = CommentsElement(driver, url_config)

    def test_check_comments(self, authorize, set_address):
        self.page.click(self.page.locators.RESTAURANTS)
        self.page.click(self.page.locators.COMMENTS_BLOCK)
        assert self.page.is_url(paths.COMMENTS_PAGE)
