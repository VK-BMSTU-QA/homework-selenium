import pytest
import time
import os.path
from selenium.webdriver.common.by import By

from ui.pages.base_page import BasePage
from ui.base_case import BaseCase


class TestMainMovieButton(BaseCase):
    authorize = True
    button_locator =  BasePage.locators.BUTTON_MAIN_MOVIE
    expected_url = "https://movie-space.ru/player/"
    # @pytest.mark.skip("SKIP")

    def test_page_switching(self):
        time.sleep(1)
        movie_url = (self.base_page.driver.find_elements_by_xpath(BasePage.locators.HREF_MAIN)[0]).get_attribute('href')
        id_movie = os.path.basename(movie_url)
        self.base_page.click(self.button_locator, 10)
        assert str(self.driver.current_url) == (self.expected_url + id_movie + "/movie")

class TestMainMovieAboutButton(BaseCase):
    authorize = True

    button_locator = BasePage.locators.BUTTON_ABOUT
    expected_url = "https://movie-space.ru/movie/"

    # @pytest.mark.skip("SKIP")
    def test_page_switching(self):
        time.sleep(1)
        movie_url = (self.base_page.driver.find_elements_by_xpath(BasePage.locators.HREF_MAIN)[0]).get_attribute('href')
        id_movie = os.path.basename(movie_url)
        self.base_page.click(self.button_locator, 10)
        assert str(self.driver.current_url) == (self.expected_url + id_movie)



