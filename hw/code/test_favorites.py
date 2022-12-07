import pytest
from ui.base_case import BaseCase
from ui.pages.series_page import SeriesPage
from ui.pages.favorites_page import FavoritesPage
from ui.pages.movie_page import MoviePage
import re


class TestFavorites(BaseCase):
    authorize = True

    like_series = SeriesPage.series_page_locators.LIKE
    favorites_series = SeriesPage.series_page_locators.BUTTON_FAVORITES
    series = FavoritesPage.locators.CARD_SERIES

    like_movies = SeriesPage.series_page_locators.LIKE
    favorites_movies = SeriesPage.series_page_locators.BUTTON_FAVORITES
    movie = FavoritesPage.locators.CARD_MOVIE

    first_title = FavoritesPage.locators.FIRST
    second_title = FavoritesPage.locators.SECOND

    favorites_like_movie = FavoritesPage.locators.LIKE_MOVIE
    favorites_like_series = FavoritesPage.locators.LIKE_SERIES

    block_movie_card = FavoritesPage.locators.BLOCK_MOVIE_CARD
    block_series_card = FavoritesPage.locators.BLOCK_SERIES_CARD

    def test_add_movie(self):
        self.serial_page.open()
        self.base_page.click(self.like_movies, 20)
        self.base_page.click(self.favorites_movies, 20)

        first = self.favorites_page.wait_visability_of_elem(self.first_title)
        assert str(first.text) == "Фильмы"

        self.base_page.click(self.movie, 20)
        assert re.match(r'^https://movie-space.ru/movie/35$', str(self.driver.current_url))

    def test_add_series(self):
        self.series_page.open()
        self.base_page.click(self.like_series, 20)
        self.base_page.click(self.favorites_series, 20)

        second = self.favorites_page.wait_visability_of_elem(self.second_title)
        assert str(second.text) == "Сериалы"

        self.base_page.click(self.series, 20)
        assert re.match(r'^https://movie-space.ru/movie/29$', str(self.driver.current_url))

    def test_delete_movie(self):
        self.favorites_page.open()
        self.base_page.click(self.favorites_like_movie, 20)

        search = (self.base_page.driver.find_elements_by_xpath(self.block_movie_card[1])[0])
        assert search.get_attribute('hidden') is not None

    def test_delete_series(self):
        self.favorites_page.open()
        self.base_page.click(self.favorites_like_series, 20)

        search = (self.base_page.driver.find_elements_by_xpath(self.block_series_card[1])[0])
        assert search.get_attribute('hidden') is not None





