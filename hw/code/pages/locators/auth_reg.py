from selenium.webdriver.common.by import By

visible = '[style="visibility: visible;"]'

class General:
    LOGIN_INPUT = (By.ID, "inputLogin")
    PASSWORD_INPUT = (By.ID, "inputPassword")
    ANY_ERROR = (By.CSS_SELECTOR, '.invalidMsg'+visible)
    LOGIN_ERROR = (By.CSS_SELECTOR, "#errorLogin"+visible)
    PASSWORD_ERROR = (By.CSS_SELECTOR, "#errorPassword"+visible)

class AuthLocators(General):
    LOGIN_BUTTON = (By.ID, "signInButton")
    REGISTER_BUTTON = (By.ID, "registration")

class RegisterLocators(General):
    FIRSTNAME_INPUT = (By.ID, "inputFirstName")
    LASTNAME_INPUT = (By.ID, "inputLastName")
    CONFIRM_PASSWORD_INPUT = (By.ID, "inputPasswordRepeat")
    REGISTER_BUTTON = (By.ID, "signupButton")
    BACK_BUTTON = (By.ID, "backButton")
    FIRSTNAME_ERROR = (By.CSS_SELECTOR, "#errorFirstName"+visible)
    LASTNAME_ERROR = (By.CSS_SELECTOR, "#errorLastName"+visible)
    CONFIRM_PASSWORD_ERROR = (By.CSS_SELECTOR, "#errorPasswordRepeat"+visible)