from selenium.webdriver.common.by import By

from pageobjects.base.page import Page
import os
import time

class MoviePage(Page):

    @property
    def __btn_enter(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__btn__input")

    @property
    def __input_email(self):
        return self.driver.find_element(by=By.ID, value="email")

    @property
    def __input_password(self):
        return self.driver.find_element(by=By.ID, value="password")

    @property
    def login_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="navbar__login-btn")

    @property
    def trailer_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="trailer__btn")

    @property
    def add_to_collection_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="movie-collection__dropdown")

    @property
    def rating_stars(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="stars__item__single-star")

    @property
    def rating_message(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="user-rating")

    @property
    def movie_rating(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="short-rating")

    @property
    def movie_review_input(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="review-input-block__text-input")

    @property
    def movie_review_submit(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="review-input-block__submit")

    @property
    def movie_review_dropdown(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="review-input-block__dropdown")

    @property
    def movie_review_success(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="review-success-block")

    @property
    def movie_bookmark_items(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="bookmark-items")

    @property
    def signup_link(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="white_text")

    @property
    def signin_link(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="review-invitation__btn")

    @property
    def first_actor(self):
        return self.driver.find_element(by=By.XPATH, value='//a[@href="/actors/90"]')

    @property
    def first_genre(self):
        return self.driver.find_element(by=By.XPATH, value='//a[@href="/genres/adventure"]')

    @property
    def first_alike_movie(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="slider__list__track__item__link")

    @property
    def first_profile(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="review-card__info__title__name")

    def __fill_email(self, email):
        self.__input_email.clear()
        self.__input_email.send_keys(email)
        self.__btn_enter.click()

    def __fill_password(self, password):
        self.__input_password.clear()
        self.__input_password.send_keys(password)
        self.__btn_enter.click()

    def __login(self, login, password):
        self.__fill_email(login)
        self.__fill_password(password)
        self.__btn_enter.click()

    def open(self, need_login=False):
        if need_login:
            super().open('login')
            self.__login(os.environ.get('AKINO_LOGIN'),
                     os.environ.get('AKINO_PASSWORD'))
            time.sleep(1)
        super().open('movies/328')

    def click_to_rating(self, rating=10):
        if rating < 1 or rating > 10:
            rating = 10
        return self.rating_stars[rating - 1].click()

    def get_rating(self):
        return float(self.movie_rating.get_property("textContent"))

    def send_review(self, text):
        self.movie_review_input.clear()
        self.movie_review_input.send_keys(text)
        self.movie_review_submit.click()


