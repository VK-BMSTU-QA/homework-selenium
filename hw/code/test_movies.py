import random
import pytest
import time
from _pytest.fixtures import FixtureRequest
import re

from ui.base_case import BaseCase
from ui.pages.movie_page import MoviePage


# class TestMoviesButtons(BaseCase):
#     authorize = True
#
#     movie_button_locator = MoviePage.locators.MOVIE_BUTTON
#
#     @pytest.mark.parametrize("button_locator, expected_url", [
#         (
#             MoviePage.locators.PERSON_PIC,
#             r'^https:\/\/movie-space.ru\/person\/\d+$'
#         ),
#         (
#             MoviePage.locators.PERSON_NAME,
#             r'^https:\/\/movie-space.ru\/person\/\d+$'
#         ),
#         (
#             MoviePage.locators.WATCH_MOVIE_BUTTON,
#             r'^https:\/\/movie-space.ru\/player\/\d+/movie$'
#         ),
#         (
#             MoviePage.locators.TRAILER_MOVIE_BUTTON,
#             r'^https:\/\/movie-space.ru\/player\/\d+/trailer$'
#         ),
#         (
#             MoviePage.locators.PREVIEW_GENRE_MOVIE_BUTTON,
#             r'^https:\/\/movie-space.ru\/genre\/\d+$'
#         ),
#         (
#             MoviePage.locators.GENRE_MOVIE_BUTTON,
#             r'^https:\/\/movie-space.ru\/genre\/\d+$'
#         ),
#     ])
#
#     def test_buttons(self, button_locator, expected_url):
#         self.movie_page.open()
#
#         self.movie_page.click(self.movie_button_locator, 15)
#         assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))
#         self.base_page.click(button_locator, 15)
#         assert re.match(expected_url, str(self.driver.current_url))


class TestPlayer(BaseCase):
    authorize = True

    movie_button_locator = MoviePage.locators.MOVIE_BUTTON
    in_player_locator = MoviePage.locators.TRAILER_MOVIE_BUTTON

    def test_exit_player(self):
        self.movie_page.open()

        self.movie_page.click(self.movie_button_locator, 15)
        assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))

        self.movie_page.click(self.in_player_locator, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+/trailer$', str(self.driver.current_url))

        self.movie_page.click(MoviePage.locators.EXIT_MOVIE_PLAYER, 15)
        assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))

    def test_left_button(self):
        self.movie_page.open()

        self.movie_page.click(self.movie_button_locator, 15)
        assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))

        self.movie_page.click(self.in_player_locator, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+/trailer$', str(self.driver.current_url))

        # self.movie_page.click(MoviePage.locators.PLAY_PAUSE_BUTTON, 60)
        #
        # time.sleep(2)
        #
        # self.movie_page.click(MoviePage.locators.RIGHT_BUTTON, 15)
        #
        # time.sleep(2)
        #
        # time_start = self.movie_page.wait_visability_of_elem(self.movie_page.locators.TIME)
        # time_start_int = int(str(time_start.text)[-2:])
        #
        # # time.sleep(2)
        #
        # self.movie_page.click(MoviePage.locators.LIFT_BUTTON, 15)
        #
        # time.sleep(2)
        #
        # time_end = self.movie_page.wait_visability_of_elem(self.movie_page.locators.TIME)
        # time_end_int = int(str(time_end.text)[-2:])
        #
        # # assert time_start_int == time_end_int
        #
        # if time_start_int < 10:
        #     assert time_end_int - time_start_int == 50
        # else:
        #     assert time_start_int - time_end_int == 10

    def test_right_button(self):
        self.movie_page.open()

        self.movie_page.click(self.movie_button_locator, 15)
        assert re.match(r'^https://movie-space.ru/movie/\d+$', str(self.driver.current_url))

        self.movie_page.click(self.in_player_locator, 15)
        assert re.match(r'^https:\/\/movie-space.ru\/player\/\d+/trailer$', str(self.driver.current_url))

        # self.movie_page.click(MoviePage.locators.PLAY_PAUSE_BUTTON, 15)
        #
        # time.sleep(2)
        #
        # time_start = self.movie_page.wait_visability_of_elem(self.movie_page.locators.TIME)
        # time_start_int = int(str(time_start.text)[-2:])
        #
        #
        # self.movie_page.click(MoviePage.locators.RIGHT_BUTTON, 15)
        #
        # time.sleep(2)
        #
        # time_end = self.movie_page.wait_visability_of_elem(self.movie_page.locators.TIME)
        # time_end_int = int(str(time_end.text)[-2:])
        #
        # # assert str(time_end.text) == str(time_start.text)
        #
        # if time_end_int < 10:
        #     assert time_start_int - time_end_int == 50
        # else:
        #     assert time_end_int - time_start_int == 10


