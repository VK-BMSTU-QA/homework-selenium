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
    BUTTON_PROFILE_1 = (By.CLASS_NAME, "name-profile")


class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[1]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[1]/input')
    PASS_LOGIN_CREDS_BUTTON = (By.CLASS_NAME, 'menu-button')
    LOGIN_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[2]')
    PASSWORD_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[2]')
    USER_DOES_NOT_EXISTS_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[3]')
    REGISTER_BUTTON = (By.XPATH, "/html/body/main/div[2]/div/div/a")

class MoviePageLocators(BasePageLocators):
    SLIDER = (By.XPATH, '//*[@id="slider"]')
    RATING = (By.XPATH, '//*[@id="rating"]')

class RegisterPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[1]/input')

    EMAIL_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[1]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[3]/div[1]/input')
    PASSWORD_COPY_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[4]/div[1]/input')
    REGISTER_BUTTON = (By.XPATH, '//*[@id="menu"]/form/button')
    LOGIN_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[2]')
    EMAIL_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[2]')
    PASSWORD_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[3]/div[2]')
    PASSWORD_COPY_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[4]/div[2]')
    USER_EXISTS_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[5]')


class ProfilePageLocators(BasePageLocators):
    LOGIN_INPUT = (
        By.XPATH,
        '//*[@id="root"]/div[3]/div/form/div[1]/div[2]/div[1]/div[1]/input',
    )
    PASSWORD_INPUT = (
        By.XPATH,
        '//*[@id="root"]/div[3]/div/form/div[1]/div[2]/div[3]/div[1]/input',
    )
    PASSWORD_COPY_INPUT = (
        By.XPATH,
        '//*[@id="root"]/div[3]/div/form/div[1]/div[2]/div[4]/div[1]/input',
    )

    PASSWORD_NOTIFICATION = (
        By.XPATH,
        '//*[@id="root"]/div[3]/div/form/div[1]/div[2]/div[3]/div[2]',
    )
    PASSWORD_COPY_NOTIFICATION = (
        By.XPATH,
        '//*[@id="root"]/div[3]/div/form/div[1]/div[2]/div[4]/div[2]',
    )

    SAVE_NOTIFICATION = (By.XPATH, '//*[@id="root"]/div[3]/div/form/div[2]')
    SAVE_BUTTON = (By.XPATH, '//*[@id="root"]/div[3]/div/form/div[3]/button')
    PROFILE_PIC = (By.CLASS_NAME, 'btn-profile')
    BUTTON_LOGOUT = (By.CLASS_NAME, 'quit')
