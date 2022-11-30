import time
from hw.code.ui.locators import basic_locators
from hw.code.ui.pages.base_page import BasePage

class MoviePage(BasePage):

    locators = basic_locators.MoviePageLocators()
    url = 'https://movie-space.ru/movies'

    def open(self):
        self.click(basic_locators.BasePageLocators.BUTTON_MOVIES, 10)
        self.is_opened(self.url, 10)
        time.sleep(1)