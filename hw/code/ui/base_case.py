import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.login import LoginPage
from ui.pages.movie_page import MoviePage
from ui.pages.series_page import SeriesPage
from ui.pages.genre_page import GenrePage

class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)

        self.movie_page = MoviePage(driver)
        self.series_page = SeriesPage(driver)
        self.genre_page = GenrePage(driver)
        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            login_page = LoginPage(driver)
            login_page.login(*credentials)
