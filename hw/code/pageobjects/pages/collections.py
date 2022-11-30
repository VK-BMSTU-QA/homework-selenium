from selenium.webdriver.common.by import By

from pageobjects.base.page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

classes = {
    "btn_logo": "navbar__logo",
    "btn_search": "search__btn",
    "btn_login": "navbar__login-btn",
    "navbar_menu": "navbar__menu",
    "btn_collections": "collections",
    "btn_genres": "genres",
    "btn_premiers": "premiers",
    "btn_single_collection": "collection",
    "btn_single_genre": "genre-poster",
    "btn_single_premier": "announced__image",
    "btn_profile" : "user-block__profile-href",
    "profile_submenu" : "user-block__submenu__block",
    "btn_logout" : "user-block__logout-btn",
    "user_block" : "user-block"
}

class CollectionsPage(Page):

    @property
    def btn_logo(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["btn_logo"])
    
    @property
    def btn_navbar_search(self):
        return self.driver.find_element(by=By.CLASS_NAME , value=classes["btn_search"])

    @property
    def btn_navbar_login(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["btn_login"])
        
    @property
    def btn_navbar_collections(self):
        return self.driver.find_element(by=By.CLASS_NAME , value=classes["navbar_menu"]).find_element(by=By.CLASS_NAME, value=classes["btn_collections"])

    @property
    def btn_navbar_genres(self):
        return self.driver.find_element(by=By.CLASS_NAME , value=classes["navbar_menu"]).find_element(by=By.CLASS_NAME, value=classes["btn_genres"])
    
    @property
    def btn_navbar_premiers(self):
        return self.driver.find_element(by=By.CLASS_NAME , value=classes["navbar_menu"]).find_element(by=By.CLASS_NAME, value=classes["btn_premiers"])

    @property
    def btn_collection(self):
        return self.driver.find_element(by=By.CLASS_NAME , value=classes["btn_single_collection"])

    @property
    def btn_premier(self):
        return self.driver.find_element(by=By.CLASS_NAME , value=classes["btn_single_premier"])

    @property
    def btn_collections_container(self):
        return len(self.driver.find_elements(by=By.CLASS_NAME , value=classes["btn_single_collection"]))

    @property
    def btn_genres_container(self):
        return len(self.driver.find_elements(by=By.CLASS_NAME , value=classes["btn_single_genre"]))

    @property
    def btn_genre(self):
        return self.driver.find_element(by=By.CLASS_NAME, value=classes["btn_single_genre"])
    
    @property
    def btn_profile(self):
        return WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, classes["btn_profile"])))

    @property
    def btn_profile_submenu(self):
        return self.driver.find_element(by=By.CLASS_NAME , value=classes["profile_submenu"])

    @property
    def btn_logout_submenu(self):
        return self.driver.find_element(by=By.CLASS_NAME , value=classes["user_block"]).find_element(by=By.CLASS_NAME, value=classes["btn_logout"])

    def open(self):
        super().open("")
