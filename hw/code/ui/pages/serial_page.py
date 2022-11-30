import time
from hw.code.ui.locators import basic_locators
from hw.code.ui.pages.series_page import SeriesPage
from hw.code.ui.pages.base_page import BasePage


class SerialPage(BasePage):
    locators = basic_locators.SeriesPageLocators()
    url = 'https://movie-space.ru/movie/29'

    def open(self):
        time.sleep(3)
        self.click(basic_locators.SeriesPageLocators.SERIAL_CARD_1, 10)
        time.sleep(3)
        self.is_opened(self.url, 10)
        time.sleep(3)
