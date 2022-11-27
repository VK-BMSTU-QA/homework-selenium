from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class LoginPage(Page):

    @property
    def btn_collection(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="collection")

    @property
    def btn_premier(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="announced__image")


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
    def btn_login(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="navbar__login-btn")

    @property
    def login_input(self):
        return self.driver.find_element(by=By.ID , value="email")

    @property
    def password_input(self):
        return self.driver.find_element(by=By.ID , value="password")

    @property
    def btn_enter(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="auth__btn__input")
    
    @property
    def btn_profile(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="user-block__profile-href")

    @property
    def btn_profile_submenu(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="user-block__submenu__block")

    @property
    def btn_logout_submenu(self):
        return self.driver.find_element(by=By.CLASS_NAME , value="user-block").find_element(by=By.CLASS_NAME, value="user-block__logout-btn")
    
    def open(self, *args, **kwargs):
        super().open("/login")

    @property
    def get_error(self):
        return self.driver.find_elements(by=By.CLASS_NAME, value="auth-input__head__error")
        

    def fill_login(self, login):
        self.login_input.send_keys(login)

    def fill_password(self, password):
        self.password_input.send_keys(password)

    def login(self, login, password):
        self.fill_login(login)
        self.fill_password(password)
        self.btn_enter.click()
