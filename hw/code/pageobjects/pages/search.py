from selenium.webdriver.common.by import By

from pageobjects.base.page import Page

class SearchPage(Page):
    def open(self, target=''):
        super().open('search/' + target)

    @property
    def movie_cards(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="movie-card")

    @property
    def person_cards(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="person-card")
    
    @property
    def no_movies(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="search-block__films-container").find_element(by=By.CLASS_NAME, value="empty-search-message")
    
    @property
    def no_persons(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="search-block__persons-container").find_element(by=By.CLASS_NAME, value="empty-search-message")
    
    @property
    def movie_img(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="movie__image")

    @property
    def person_img(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="person__image")

    @property
    def empty_msg(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="error-message")
