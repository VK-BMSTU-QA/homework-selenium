from selenium.webdriver.common.by import By


class BasePageLocators:
    CARD = (By.XPATH, '//*[@id="35"]')
    BUTTON_SEARCH = (By.XPATH, "//*[@id='header']/div[1]/div[4]//*[local-name() = 'svg'][1]")
    BUTTON_CLOSE_SEARCH = (By.XPATH, "//*[@id='header']/div[1]/div[4]//*[local-name() = 'svg'][2]")
    INPUT_SEARCH = (By.XPATH, '//*[@id="live-search"]')
    TOPIC = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div')
    TITLE_TOPIC = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div/a')
    RES_TOPIC = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div[1]/div/a[1]')
    RES_TOPICS = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div/div/a[1]')
    EMPTY_TOPIC = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div')

class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[1]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[1]/input')
    PASS_LOGIN_CREDS_BUTTON = (By.XPATH, '//*[@id="menu"]/form/button')

class MoviePageLocators(BasePageLocators):
    SLIDER = (By.XPATH, '//*[@id="slider"]')
    RATING = (By.XPATH, '//*[@id="rating"]')

