import pytest
import time
from ui.pages.base_page import BasePage
from ui.base_case import BaseCase

class TestHeaderButtons(BaseCase):
    authorize = True

    @pytest.mark.parametrize("button_locator, expected_url", [
        (
            BasePage.locators.BUTTON_MOVIES, 
            'https://movie-space.ru/movies'
        ),
        (
            BasePage.locators.BUTTON_SERIES, 
            'https://movie-space.ru/series'
        ),
        (
            BasePage.locators.BUTTON_GENRES, 
            'https://movie-space.ru/genre/1'
        ),
        (
            BasePage.locators.BUTTON_FAVORITES, 
            'https://movie-space.ru/favorites'
        ),
        (
            BasePage.locators.BUTTON_PROFILE_1, 
            'https://movie-space.ru/profile'
        ),
        ])
    
    def test_page_switching(self, button_locator,expected_url):
        self.base_page.click(button_locator, 10)
        assert str(self.driver.current_url) == expected_url

class TestMainPageButtons(BaseCase):
    authorize = True

    movie_button_locator = BasePage.locators.BUTTON_MOVIES 
    movie_url = 'https://movie-space.ru/movies'

    @pytest.mark.parametrize("button_locator, expected_url", [
        (
            BasePage.locators.BUTTON_MAIN, 
            'https://movie-space.ru/'
        ),
        (
            BasePage.locators.BUTTON_LOGO, 
            'https://movie-space.ru/'
        ),
        ])
    
    def test_page_switching(self, button_locator,expected_url):
        self.base_page.click(self.movie_button_locator, 10)
        assert str(self.driver.current_url) == self.movie_url
        self.base_page.click(button_locator, 10)
        assert str(self.driver.current_url) == expected_url



class TestProfileButtons(BaseCase):
    authorize = True

    @pytest.mark.parametrize("button_locator, expected_url", [
        (
            BasePage.locators.BUTTON_PROFILE_2, 
            'https://movie-space.ru/profile'
        ),
        (
            BasePage.locators.BUTTON_SUBSCRIPTION, 
            'https://movie-space.ru/subscription'
        ),
        (
            BasePage.locators.BUTTON_LOGOUT, 
            'https://movie-space.ru/login'
        ),
        ])

    def test_profile_buttons(self, button_locator, expected_url):
        self.base_page.move_on_element(BasePage.locators.PROFILE_PIC, 3)
        self.base_page.click(button_locator, 10)
        assert str(self.driver.current_url) == expected_url
