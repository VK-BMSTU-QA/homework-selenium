from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class ProfilePage(Page):
    @property
    def btn_change(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="profile-info__container__settings")

    @property
    def btn_save_name(self):
        return self.driver.find_element_by_xpath("//input[@value='Сохранить']")

    @property
    def btn_close_settings(self):
        return self.driver.find_element_by_xpath("//input[@value='Отменить']")

    @property
    def input_name(self):
        return self.driver.find_element_by_xpath("//input[@name='username']")

    @property
    def name(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="name")

    @property
    def btn_single_bookmark(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="bookmark-element")

    @property
    def btn_movie_poster(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="review__image")

    @property
    def error_text(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="profile-info__container__settings__form__name-error").text

    @property
    def btn_popup_open(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="bookmark-element-default")

    @property
    def popup_container(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="profile__popup__container__body")

    @property
    def btn_popup_close(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="popup-close")

    @property
    def input_popup(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="bookmark-name")

    @property
    def btn_create_bookmark(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="bookmark-submit")

    def bookmark_title(self, name):
        List = self.driver.find_elements(by=By.CLASS_NAME, value="bookmark-element__description")
        for i in List:
            if i.text == name:
                return True
        return False

    def open(self, *args, **kwargs):
        super().open("/profile/115")

