import random
import pytest
import time
from _pytest.fixtures import FixtureRequest
import re

from ui.base_case import BaseCase
from ui.pages.series_page import SeriesPage


class TestSeriesButtons(BaseCase):
    authorize = True

    series_button_locator = SeriesPage.locators.SERIES_BUTTON

    @pytest.mark.parametrize("button_locator, expected_url", [
        (
            SeriesPage.locators.PERSON_PIC,
            r'^https:\/\/movie-space.ru\/person\/\d+$'
        ),
        (
            SeriesPage.locators.PERSON_NAME,
            r'^https:\/\/movie-space.ru\/person\/\d+$'
        ),
        (
            SeriesPage.locators.WATCH_SERIES_BUTTON,
            r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=1$'
        ),
        (
            SeriesPage.locators.TRAILER_SERIES_BUTTON,
            r'^https:\/\/movie-space.ru\/player\/\d+/trailer$'
        ),
        (
            SeriesPage.locators.PREVIEW_GENRE_SERIES_BUTTON,
            r'^https:\/\/movie-space.ru\/genre\/\d+$'
        ),
        (
            SeriesPage.locators.GENRE_SERIES_BUTTON,
            r'^https:\/\/movie-space.ru\/genre\/\d+$'
        ),
        (
            SeriesPage.locators.EPISODE_2,
            r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=2$'
        ),
    ])

    def test_buttons(self, button_locator, expected_url):
        self.series_page.open()

        self.series_page.click(self.series_button_locator, 15)
        assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))
        self.base_page.click(button_locator, 15)
        assert re.match(expected_url, str(self.driver.current_url))


class TestPlayer(BaseCase):
    authorize = True

    series_button_locator = SeriesPage.locators.SERIES_BUTTON
    in_player_locator = SeriesPage.locators.WATCH_SERIES_BUTTON

    def test_next_episode(self):
        self.series_page.open()

        self.series_page.click(self.series_button_locator, 15)
        assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))

        self.series_page.click(self.in_player_locator, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=1$', str(self.driver.current_url))

        self.series_page.click(SeriesPage.locators.NEXT_EPISODE, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=2$', str(self.driver.current_url))

    def test_prev_episode(self):
        self.series_page.open()

        self.series_page.click(self.series_button_locator, 15)
        assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))

        self.series_page.click(self.in_player_locator, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=1$', str(self.driver.current_url))

        self.series_page.click(SeriesPage.locators.NEXT_EPISODE, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=2$', str(self.driver.current_url))

        self.series_page.click(SeriesPage.locators.PREV_EPISODE, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=1$', str(self.driver.current_url))

    def test_choice_episode(self):
        self.series_page.open()

        self.series_page.click(self.series_button_locator, 15)
        assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))

        self.series_page.click(self.in_player_locator, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=1$', str(self.driver.current_url))

        self.series_page.move_on_element(self.series_page.locators.EPISODES, 5)

        self.series_page.click(self.series_page.locators.PLAYER_EPISODE_2, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+\?seas=1&ep=2$', str(self.driver.current_url))