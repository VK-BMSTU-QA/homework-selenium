from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class ProfilePage(Page):

    
    
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
        super().open("/profile")
