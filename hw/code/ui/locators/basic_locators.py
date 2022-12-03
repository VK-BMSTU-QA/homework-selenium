from selenium.webdriver.common.by import By


class BasePageLocators:
    QUERY_LOCATOR = (By.NAME, "q")
    QUERY_LOCATOR_ID = (By.ID, "id-search-field")
    GO_BUTTON_LOCATOR = (By.XPATH, '//*[@id="submit"]')
    START_SHELL = (By.ID, "start-shell")
    PYTHON_CONSOLE = (By.ID, "hterm:row-nodes")

    BUTTON_PROFILE_1 = (By.CLASS_NAME, "name-profile")

    PROFILE_PIC = (By.XPATH, '//*[@id="header"]/div[1]/div[5]')

    PROFILE_MENU = (By.XPATH, '//*[@id="root"]/div/header/div[5]/div/div[2]')

    BUTTON_PROFILE_2 = (By.XPATH, '//*[@id="header"]/div[1]/div[5]/div/div[2]/a[1]')
    BUTTON_LOGOUT = (By.XPATH, '//*[@id="header"]/div[1]/div[5]/div/div[2]/a[3]')


class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[1]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[1]/input')
    PASS_LOGIN_CREDS_BUTTON = (By.XPATH, '//*[@id="menu"]/form/button')
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
    PROFILE_PIC = (By.XPATH, '//*[@id="root"]/div[1]/div[5]/div/div[1]')
    BUTTON_LOGOUT = (By.XPATH, '//*[@id="root"]/div[1]/div[5]/div/div[2]/a[3]')
