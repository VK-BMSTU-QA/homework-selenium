import time
from ui.locators import basic_locators
from ui.pages.base_page import BasePage


class SeriesPage(BasePage):
    locators = basic_locators.SeriesPageLocators()
    url = 'https://movie-space.ru/series'

    def open(self):
        self.click(basic_locators.BasePageLocators.BUTTON_SERIES, 10)
        self.is_opened(self.url, 10)
        time.sleep(1)
