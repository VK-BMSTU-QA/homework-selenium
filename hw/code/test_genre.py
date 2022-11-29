import random
import pytest
import time
from _pytest.fixtures import FixtureRequest
import re

from ui.base_case import BaseCase
from ui.pages.genre_page import GenrePage


class TestGenreButtons(BaseCase):
    authorize = True

    def test_open_sport(self):
        self.genre_page.open()

        self.genre_page.click(GenrePage.locators.SPORT, 15)

        assert "https://movie-space.ru/genre/16" == str(self.driver.current_url)
