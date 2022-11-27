from pageobjects.pages.search import SearchPage
from tests.base_test_case import BaseTestCase


class SearchTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = SearchPage(self.driver)

    def test_no_movies(self):
        self.page.open('wriptjgnevevenv')
        tmp = self.page.no_movies
        self.assertEqual(tmp.text, 'Упс, ничего не найдено', 'No movies found')

    def test_no_actors(self):
        self.page.open('wriptjgnevevenv')
        tmp = self.page.no_persons
        self.assertEqual(tmp.text, 'Упс, ничего не найдено', 'No actors found')

    def test_movie(self):
        self.page.open('speed')
        self.page.movie_img.click()
        self.assertTrue(
            'https://park-akino.ru/movies/' in self.page.driver.current_url, 'Movie test')

    def test_person(self):
        self.page.open('tricky')
        self.page.person_img.click()
        self.assertTrue(
            'https://park-akino.ru/actors/' in self.page.driver.current_url, 'Actors test')

    def test_empty(self):
        self.page.open()
        tmp = self.page.empty_msg
        self.assertEqual(
            tmp.text, 'Запрос некорректен, попробуйте ещё раз', 'Empty search request')
