import pytest
from _pytest.fixtures import FixtureRequest

from ui.pages.base_page import BasePage
from ui.pages.login import LoginPage
from ui.pages.movie_page import MoviePage
from ui.pages.profile_page import ProfilePage
from ui.pages.register import RegPage
from ui.pages.series_page import SeriesPage
from ui.pages.player import Player
from ui.pages.favorites_page import FavoritesPage



class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config
        self.base_page = BasePage(driver)
        self.login_page = LoginPage(driver)
        self.serial_page = MoviePage(driver)
        self.profile_page = ProfilePage(driver)
        self.reg_page = RegPage(driver)
        self.series_page = SeriesPage(driver)
        self.player = Player(driver)
        self.favorites_page = FavoritesPage(driver)
        if self.authorize:
            credentials = request.getfixturevalue('credentials')
            login_page = LoginPage(driver)
            login_page.login(*credentials)
