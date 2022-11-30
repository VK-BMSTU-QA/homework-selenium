import pytest
from _pytest.fixtures import FixtureRequest

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.pages.login import LoginPage
from hw.code.ui.pages.movie_page import MoviePage
from hw.code.ui.pages.serial_page import SerialPage
from hw.code.ui.pages.series_page import SeriesPage

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.series_page = SeriesPage(driver)
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.serial_page = SerialPage(driver)
        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            login_page = LoginPage(driver)
            login_page.login(*credentials)
