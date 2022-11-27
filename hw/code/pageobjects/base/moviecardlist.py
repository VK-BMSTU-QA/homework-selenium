from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class MovieCardListPage(Page):
    def open(self, url):
        super().open(url)

    @property
    def movie_cards(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="movie-card")

    @property
    def movie_img(self):
        return self.movie_cards[0].find_element(by=By.CLASS_NAME, value="movie__image")
