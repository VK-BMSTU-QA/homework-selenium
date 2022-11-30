from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import os
import time

from pageobjects.base.page import Page


class BookmarkPage(Page):
    @property
    def bookmark_elements(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="bookmark-element")

    @property
    def __btn_enter(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__btn__input")

    @property
    def __input_email(self):
        return self.driver.find_element(by=By.ID, value="email")

    @property
    def __input_password(self):
        return self.driver.find_element(by=By.ID, value="password")

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

    def open(self):
        super().open('login')
        self.__login(os.environ.get('AKINO_LOGIN'),
                     os.environ.get('AKINO_PASSWORD'))
        time.sleep(1)
        super().open('profile/115')
        self.bookmark_elements[0].click()

    @property
    def movie_img(self):
        try:
            return self.driver.find_element(by=By.CLASS_NAME, value="movie__image")
        finally:
            return None

    @property
    def remove_movie_btn(self):
        try:
            return self.driver.find_element(by=By.CLASS_NAME, value="movie__body__info__data__title__delete-movie-btn")
        finally:
            return None

    @property
    def notify_msg(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="notify__message")

    @property
    def movie_cards(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="movie-card")

    @property
    def bookmark_title(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="container__bookmark-title__color__title-user")

    def change_title(self, newtitle):
        tmp = self.bookmark_title
        tmp.send_keys(newtitle)
        tmp.send_keys(Keys.ENTER)

    @property
    def popup(self):
        try:
            return WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located((By.CLASS_NAME, 'popup-open')))
        except TimeoutException:
            return None

    @property
    def notify_msg(self):
        return WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located((By.CLASS_NAME, 'notify__message')))

    @property
    def remove_bookmark_btn(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="container__bookmark-settings__delete-playlist-btn")

    @property
    def popup_sub_btn(self):
        return WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located((By.CLASS_NAME, 'bookmark-submit')))

    @property
    def popup_cancel_btn(self):
        return WebDriverWait(self.driver, 1).until(ec.visibility_of_element_located((By.CLASS_NAME, 'bookmark-cancel')))
