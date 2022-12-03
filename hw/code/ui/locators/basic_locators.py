from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_PROFILE_1 = (By.CLASS_NAME, "name-profile")

class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[1]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[1]/input')
    PASS_LOGIN_CREDS_BUTTON = (By.CLASS_NAME, 'menu-button')
    LOGIN_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[2]')
    PASSWORD_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[2]')
    USER_DOES_NOT_EXISTS_NOTIFICATION = (By.XPATH, '//*[@id="menu"]/form/div[3]')
    REGISTER_BUTTON = (By.XPATH, "/html/body/main/div[2]/div/div/a")

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
