import time
from hw.code.ui.locators import basic_locators

from hw.code.ui.pages.base_page import BasePage


class MoviePage(BasePage):
    locators = basic_locators.MoviePageLocators()
    url = 'https://movie-space.ru/movie/35'

    def open(self):
        self.click(BasePage.locators.CARD, 10)
        self.wait_visability_of_elem(
            self.locators.RATING, 10
        )

