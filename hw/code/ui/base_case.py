import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.profile_page import ProfilePage
from ui.pages.base_page import BasePage
from ui.pages.login import LoginPage
from ui.pages.register import RegPage


class BaseCase:
    authorize = True

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page = BasePage(driver)
        self.profile_page = ProfilePage(driver)
        self.reg_page = RegPage(driver)
        self.login_page = LoginPage(driver)
        if self.authorize:
            credentials = request.getfixturevalue("credentials")
            login_page = LoginPage(driver)
            login_page.login(*credentials)
