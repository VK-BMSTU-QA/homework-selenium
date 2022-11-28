from pageobjects.pages.movie import MoviePage
from tests.base_test_case import BaseTestCase
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import math
import os

MAX_REVIEW_LENGTH = 300

class MovieTest(BaseTestCase):
    def setUp(self):
        super().setUp()
        self.page = MoviePage(self.driver)

    def test_movie_add_to_collection_button(self):
        self.page.open(need_login=True)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(self.page.add_to_collection_btn))

    def test_movie_rating_message(self):
        self.page.open(need_login=True)
        self.page.click_to_rating(10)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "user-rating"),
            "Ваша оценка: 10. Рейтинг фильма:"
        ))

    def test_movie_rating_value(self):
        self.page.open(need_login=True)
        old_rating = self.page.get_rating()
        self.page.click_to_rating(math.ceil(old_rating))
        new_rating = self.page.get_rating()
        self.assertGreaterEqual(new_rating, old_rating)

    def test_movie_review_buttons(self):
        self.page.open(need_login=True)
        wait = WebDriverWait(self.driver, 10)
        if not self.page.movie_review_success.is_displayed():
            wait.until(EC.visibility_of(self.page.movie_review_dropdown))
            wait.until(EC.visibility_of(self.page.movie_review_input))
            wait.until(EC.visibility_of(self.page.movie_review_submit))
        else:
            wait.until(EC.visibility_of(self.page.movie_review_success))

    def test_movie_review_max_text(self):
        self.page.open(need_login=True)
        wait = WebDriverWait(self.driver, 10)
        if not self.page.movie_review_success.is_displayed():
            self.page.movie_review_input.clear()
            self.page.movie_review_input.send_keys("0" * (MAX_REVIEW_LENGTH + 10))
            self.assertEqual(len(self.page.movie_review_input.value), MAX_REVIEW_LENGTH)
            self.page.movie_review_submit.click()
        wait.until(EC.visibility_of(self.page.movie_review_success))

    def test_movie_review_average_len_text(self):
        self.page.open(need_login=True)
        wait = WebDriverWait(self.driver, 10)
        if not self.page.movie_review_success.is_displayed():
            self.page.movie_review_input.clear()
            self.page.movie_review_input.send_keys("0" * (MAX_REVIEW_LENGTH // 2))
            self.assertEqual(len(self.page.movie_review_input.value), MAX_REVIEW_LENGTH)
            self.page.movie_review_submit.click()
        wait.until(EC.visibility_of(self.page.movie_review_success))

    def test_collection_dropdown(self):
        self.page.open(need_login=True)
        wait = WebDriverWait(self.driver, 10)
        wait.until_not(EC.visibility_of(self.page.movie_bookmark_items))
        self.page.add_to_collection_btn.click()
        wait.until(EC.visibility_of(self.page.movie_bookmark_items))

    def test_movie_trailer(self):
        self.page.open()
        self.page.trailer_btn.click()
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.url_contains("youtube"))

    def test_unauth_rating_click(self):
        self.page.open()
        self.page.click_to_rating(10)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "user-rating"),
            "Чтобы поставить оценку, пожалуйста,"
        ))

    def test_rating_to_signup(self):
        self.page.open()
        self.page.click_to_rating(10)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "user-rating"),
            "Чтобы поставить оценку, пожалуйста,"
        ))
        self.page.signup_link.click()
        wait.until(EC.url_contains("register"))

    def test_unauth_review(self):
        self.page.open()
        self.page.click_to_rating(10)
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of(self.page.signin_link))

    def test_unauth_review_to_signin(self):
        self.page.open()
        self.page.click_to_rating(10)
        wait = WebDriverWait(self.driver, 10)
        self.page.signin_link.click()
        wait.until(EC.url_contains("login"))

    def test_movie_to_actor(self):
        self.page.open()
        wait = WebDriverWait(self.driver, 10)
        self.page.first_actor.click()
        wait.until(EC.url_contains("actors"))

    def test_movie_to_genre(self):
        self.page.open()
        wait = WebDriverWait(self.driver, 10)
        self.page.first_genre.click()
        wait.until(EC.url_contains("genres"))

    def test_movie_to_alike_movie(self):
        self.page.open()
        wait = WebDriverWait(self.driver, 10)
        self.page.first_alike_movie.click()
        wait.until(EC.url_contains("movies"))

    def test_movie_to_profile(self):
        self.page.open()
        wait = WebDriverWait(self.driver, 10)
        self.page.first_profile.click()
        wait.until(EC.url_contains("profile"))
