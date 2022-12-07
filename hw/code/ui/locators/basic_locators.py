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
    BUTTON_SERIES = (By.XPATH, '//*[@id="header"]/div[1]/div[2]/a[3]')
    BUTTON_FAVORITES = (By.XPATH, '//*[@id="header"]/div[1]/div[2]/a[5]')


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
    LIKE = (By.CLASS_NAME, 'like')
    BUTTON_FAVORITES = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/a[5]')

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


class AllSeriesPageLocators(BasePageLocators):
    CARD = (By.XPATH, '//*[@id="29"]')

class SeriesPageLocators(BasePageLocators):
    PLAY_BUTTON = (By.CLASS_NAME, 'play-button')
    LIKE = (By.CLASS_NAME, 'like')
    BUTTON_FAVORITES = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/a[5]')

class PlayerLocators(BasePageLocators):
    PAUSE_SVG = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/button[1]//*[local-name() = 'svg'][2]")
    PLAY_SVG = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/button[1]//*[local-name() = 'svg'][1]")
    PLAY_PAUSE_BUTTON = (By.CLASS_NAME, 'play-pause')

    LEFT_BUTTON = (By.CLASS_NAME, 'rewind')
    RIGHT_BUTTON = (By.CLASS_NAME, 'forward')

    TIME = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]')

    SOUND_BUTTON = (By.CLASS_NAME, 'volume')
    FULL_SOUND_SVG = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/button[4]//*[local-name() = 'svg'][1]")
    MUTE_SOUND_SVG = (By.XPATH, "//*[@id='root']/div/div[2]/div[2]/button[4]//*[local-name() = 'svg'][3]")

class FavoritesPageLocators(BasePageLocators):
    FAVORITES_TEXT = (By.CLASS_NAME, 'favorite__text')
    CARD_SERIES = (By.XPATH, '//*[@id="29"]')
    CARD_MOVIE = (By.XPATH, '//*[@id="35"]')
    FIRST = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[1]/div[1]/div')
    SECOND = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[2]/div[1]/div')
    LIKE_MOVIE = (By.XPATH, '//*[@id="like_35"]')
    LIKE_SERIES = (By.XPATH, '//*[@id="like_29"]')
    BLOCK_MOVIE_CARD = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[1]/div[2]/div/div/div')
    BLOCK_SERIES_CARD = (By.XPATH, '//*[@id="root"]/div/div/div[3]/div/div[1]/div[2]/div/div/div')