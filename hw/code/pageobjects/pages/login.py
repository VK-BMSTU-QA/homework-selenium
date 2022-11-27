from selenium.webdriver.common.by import By

from pageobjects.base.page import Page


class LoginPage(Page):


    @property
    def member_link(self):
        # return self.driver.find_element(by=By.CLASS_NAME, value="github-hrefs")[1].text
        return self.driver.find_element_by_link_text("Киселев Виктор")
    
    @property
    def GH_image(self):
        # return self.driver.find_element(by=By.CLASS_NAME, value="github-hrefs")[1].text
        footer = self.driver.find_element(by=By.ID, value="footer")
        social = footer.find_element(by=By.CLASS_NAME, value="social")
        return social.find_element_by_xpath('img')

    @property
    def btn_enter(self):
        return self.driver.find_element(by=By.CLASS_NAME, value="auth__btn__input")

    @property
    def input_email(self):
        return self.driver.find_element(by=By.ID, value="email")

    @property
    def input_password(self):
        return self.driver.find_element(by=By.ID, value="password")
    
    def get_error_email(self):
        input =  self.driver.find_element(by=By.ID, value="email")
        td_p_input = input.find_element_by_xpath('..')
        return td_p_input.find_element(by=By.CLASS_NAME, value="email").text

    def get_error_password(self):
        input =  self.driver.find_element(by=By.ID, value="password")
        td_p_input = input.find_element_by_xpath('..')
        return td_p_input.find_element(by=By.CLASS_NAME, value="password").text
        
    def open(self, *args, **kwargs):
        super().open("login")

    def go_to_link(self):
        self.member_link.click()

    def go_to_GH(self):
        self.GH_image.click()

    def fill_email(self, email):
        self.input_email.clear()
        self.input_email.send_keys(email)
        self.btn_enter.click()

    def fill_password(self, password):
        self.input_password.clear()
        self.input_password.send_keys(password)
        self.btn_enter.click()
    
    def login(self, login, password):
        self.fill_email(login)
        self.fill_password(password)
        self.btn_enter.click()
