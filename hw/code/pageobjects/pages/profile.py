from selenium.webdriver.common.by import By

from pageobjects.base.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


classes = {
    "btn_change_name": "profile-info__container__settings",
    "btn_profile" : "user-block__profile-href",
    "profile_name" : "name",
    "btn_single_bookmark" : "bookmark-element",
    "profile_movie_poster" : "review__image",
    "error_text" : "profile-info__container__settings__form__name-error",
    "btn_open_popup" : "bookmark-element-default",
    "popup_container" : "profile__popup__container__body",
    "btn_popup_close" : "popup-close",
    "input_popup" : "bookmark-name",
    "btn_create_bookmark" : "bookmark-submit",
    "bookmark_title" : "bookmark-element__description"
}

xpathes = {
    "btn_save" : "//input[@value='Сохранить']",
    "btn_close_settings" : "//input[@value='Отменить']",
    "input_name" : "//input[@name='username']"
}

testProfileLink = "/profile/115"

class ProfilePage(Page):
    @property
    def btn_change(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["btn_change_name"])

    @property
    def btn_save_name(self):
        return self.driver.find_element(by=By.XPATH, value=xpathes["btn_save"])

    @property
    def btn_close_settings(self):
        return self.driver.find_element(by=By.XPATH, value=xpathes["btn_close_settings"])

    @property
    def input_name(self):
        return self.driver.find_element(by=By.XPATH, value=xpathes["input_name"])

    @property
    def name(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["profile_name"])

    @property
    def btn_single_bookmark(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["btn_single_bookmark"])

    @property
    def btn_movie_poster(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["profile_movie_poster"])

    @property
    def error_text(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["error_text"]).text

    @property
    def btn_popup_open(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["btn_open_popup"])

    @property
    def popup_container(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, classes["popup_container"])))

    @property
    def btn_popup_close(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["btn_popup_close"])

    @property
    def input_popup(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["input_popup"])

    @property
    def btn_create_bookmark(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["btn_create_bookmark"])

    @property
    def bookmark_title(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_all_elements_located((By.CLASS_NAME, classes["bookmark_title"])))

    @property
    def btn_profile(self):
        return WebDriverWait(self.driver, 8).until(ec.visibility_of_element_located((By.CLASS_NAME, classes["btn_profile"])))

    def open(self):
        super().open(testProfileLink)

