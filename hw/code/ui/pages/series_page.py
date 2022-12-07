import time
from ui.locators import basic_locators
from ui.pages.base_page import BasePage

class SeriesPage(BasePage):

    locators = basic_locators.AllSeriesPageLocators()
    series_page_locators = basic_locators.SeriesPageLocators()

    def open(self):
        self.click(BasePage.locators.BUTTON_SERIES, 10)
        self.wait_visability_of_elem(
            self.locators.CARD, 10
        )

        self.click(self.locators.CARD, 10)
        self.wait_visability_of_elem(
            self.series_page_locators.PLAY_BUTTON, 10
        )

        # self.click(self.locators.CARD, 10)
        # self.wait_visability_of_elem(
        #     self.locators.RATING, 10
        # )