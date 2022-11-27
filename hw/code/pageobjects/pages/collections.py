from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class CollectionsPage(Page):

@property
    def btn_logo(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="navbar__logo")

    @property
    def btn_navbar_collections(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__menu").find_element(by=By.CLASS_NAME, value="collections")

    @property
    def btn_navbar_genres(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__menu").find_element(by=By.CLASS_NAME, value="genres")
    
    @property
    def btn_navbar_premiers(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__menu").find_element(by=By.CLASS_NAME, value="premiers")
    
    @property
    def btn_navbar_search(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="search__btn")

    @property
    def btn_collection(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="collection")

    @property
    def btn_premier(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="announced__image")

    @property
    def btn_genres(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__menu").find_element(by=By.CLASS_NAME, value="genres")

    @property
    def btn_collections_container(self):
        return len(self.driver.find_elements(by=By.CLASS_NAME , value="collection"))

    @property
    def btn_genres_container(self):
        return len(self.driver.find_elements(by=By.CLASS_NAME , value="genre-poster"))

    @property
    def btn_genre(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="genre-poster")
    
    @property
    def btn_premiers(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__menu").find_element(by=By.CLASS_NAME, value="premiers")

    def open(self, *args, **kwargs):
        super().open("")

