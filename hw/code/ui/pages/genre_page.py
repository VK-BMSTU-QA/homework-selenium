import time
from ui.locators import basic_locators
from ui.pages.base_page import BasePage

class GenrePage(BasePage):

    locators = basic_locators.GenrePageLocators()
    url = 'https://movie-space.ru/genre/1'

    def open(self):
        self.click(basic_locators.BasePageLocators.BUTTON_GENRES, 10)
        self.is_opened(self.url, 10)
        time.sleep(1)

