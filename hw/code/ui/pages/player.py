import time
from ui.locators import basic_locators
from ui.pages.series_page import SeriesPage

class Player(SeriesPage):
    player_locators = basic_locators.PlayerLocators()

    def open_player(self):
        self.open()
        self.click(self.series_page_locators.PLAY_BUTTON, 10)
        self.wait_visability_of_elem(
            self.player_locators.PLAY_PAUSE_BUTTON, 10
        )