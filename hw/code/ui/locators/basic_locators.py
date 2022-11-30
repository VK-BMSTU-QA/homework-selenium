from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_MAIN_MOVIE = (By.XPATH, '//*[@id="header"]/div[2]/div/button')
    BUTTON_ABOUT = (By.XPATH, '//*[@id="header"]/div[2]/div/a')
    BUTTON_LOGO = (By.XPATH, '//*[@id="root"]/div[1]/a[1]')
    BUTTON_MAIN = (By.XPATH, '//*[@id="root"]/div[1]/div[2]/a[1]')
    HREF_MAIN = '//*[@id="header"]/div[2]/div/a'
    BUTTON_LIKE = (By.XPATH, '//*[@id="like_35"]')
    CARD = (By.XPATH, '//*[@id="35"]')
    BUTTON_SERIES = (By.XPATH, '//*[@id="header"]/div[1]/div[2]/a[3]')
    BUTTON_ARROW_RIGHT = (By.XPATH, '//*[@id="nextBtn"]')
    BUTTON_ARROW_LEFT = (By.XPATH, '//*[@id="prevBtn"]')
    SELECTION = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[1]/div[2]')
    CHILD_SELECTION = (By.XPATH, '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div/div')
    BUTTON_SEARCH = (By.XPATH, "//*[@id='header']/div[1]/div[4]//*[local-name() = 'svg'][1]")
    BUTTON_CLOSE_SEARCH = (By.XPATH, "//*[@id='header']/div[1]/div[4]//*[local-name() = 'svg'][2]")
    INPUT_SEARCH = (By.XPATH, '//*[@id="live-search"]')
    TOPIC = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div')
    TITLE_TOPIC = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div/a')
    RES_TOPIC = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div/div/a[1]')
    EMPTY_TOPIC = (By.XPATH, '//*[@id="header"]/div[1]/div[4]/div/form/div/div')
class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[1]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[1]/input')
    PASS_LOGIN_CREDS_BUTTON = (By.XPATH, '//*[@id="menu"]/form/button')


class MoviePageLocators(BasePageLocators):
    PERSON_PIC = (By.XPATH, '//*[@id="root"]/div[8]/div[2]/div[1]/a/div[1]')
    PERSON_NAME = (By.XPATH, '//*[@id="root"]/div[8]/div[2]/div[1]/a/div[2]')
    MOVIE_BUTTON = (By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[1]/div/a')
    WATCH_MOVIE_BUTTON = (By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[4]/button')
    TRAILER_MOVIE_BUTTON = (By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[4]/a')
    PREVIEW_GENRE_MOVIE_BUTTON = (By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[3]/a[1]')
    GENRE_MOVIE_BUTTON = (By.XPATH, '//*[@id="root"]/div[7]/div[2]/a[1]')
    EXIT_MOVIE_PLAYER = (By.XPATH, '//*[@id="root"]/div/a')
    PAUSE_SVG = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[1]/svg[2]')
    PLAY_SVG = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[1]/svg[1]')
    PLAY_PAUSE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[1]')

    LIFT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[2]')
    RIGHT_BUTTON = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[3]')

    TIME = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]')


class SeriesPageLocators(BasePageLocators):
    PARENT_EPISODE_CARD = (By.XPATH, '//*[@id="root"]/div[5]/div[1]/div[2]/div/div/div[1]')
    EPISODE_CARD = (By.XPATH, '//*[@id="236"]')
    SERIAL_CARD_1 = (By.XPATH, '//*[@id="29"]')
    SLIDER = (By.XPATH, '//*[@id="slider"]')
    RATING = (By.XPATH, '//*[@id="rating"]')
class PlayerLocators(BasePageLocators):
    OPEN_ALL = (By.XPATH, '//*[@id="root"]/div[4]')
    SPORT = (By.XPATH, '//*[@id="root"]/div[3]/a[15]')


class GenrePageLocators(BasePageLocators):
    OPEN_ALL = (By.XPATH, '//*[@id="root"]/div[4]')
    SPORT = (By.XPATH, '//*[@id="root"]/div[3]/a[15]')
