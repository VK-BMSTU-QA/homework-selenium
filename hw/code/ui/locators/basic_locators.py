from selenium.webdriver.common.by import By

class BasePageLocators:
    BUTTON_MOVIES = (By.XPATH, '//*[@id="header"]/div[1]/div[2]/a[2]')
    BUTTON_SERIES = (By.XPATH, '//*[@id="header"]/div[1]/div[2]/a[3]')
    BUTTON_GENRES = (By.XPATH, '//*[@id="header"]/div[1]/div[2]/a[4]')

class LoginPageLocators(BasePageLocators):
    LOGIN_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[1]/div[1]/input')
    PASSWORD_INPUT = (By.XPATH, '//*[@id="menu"]/form/div[2]/div[1]/input')
    PASS_LOGIN_CREDS_BUTTON = (By.XPATH, '//*[@id="menu"]/form/button')

class MoviePageLocators(BasePageLocators):
    PERSON_PIC  = (By.XPATH, '//*[@id="root"]/div[8]/div[2]/div[1]/a/div[1]')
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

    LIFT_BUTTON =(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[2]')
    RIGHT_BUTTON =(By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[3]')

    TIME = (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]')

class SeriesPageLocators(BasePageLocators):
    PERSON_PIC  = (By.XPATH, '//*[@id="root"]/div[8]/div[2]/div[1]/a/div[1]')
    PERSON_NAME = (By.XPATH, '//*[@id="root"]/div[8]/div[2]/div[1]/a/div[2]')
    SERIES_BUTTON = (By.XPATH, '//*[@id="root"]/div[3]/div/div[1]/div/a')
    WATCH_SERIES_BUTTON = (By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[4]/button')
    TRAILER_SERIES_BUTTON = (By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[4]/a')
    PREVIEW_GENRE_SERIES_BUTTON = (By.XPATH, '//*[@id="root"]/div[3]/div[2]/div[3]/a[1]')
    GENRE_SERIES_BUTTON = (By.XPATH, '//*[@id="root"]/div[7]/div[2]/a[1]')
    EPISODE_2 = (By.XPATH, '//*[@id="root"]/div[5]/div[1]/div[2]/div/div/div[2]/div[1]')

    NEXT_EPISODE = (By.XPATH, '//*[@id="root"]/div/a[2]')
    PREV_EPISODE = (By.XPATH, '//*[@id="root"]/div/a[2]')

    EPISODES = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[5]')
    PLAYER_EPISODE_2 = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/button[5]/div/div/div/a[2]')

class PlayerLocators(BasePageLocators):
    OPEN_ALL  = (By.XPATH, '//*[@id="root"]/div[4]')
    SPORT = (By.XPATH, '//*[@id="root"]/div[3]/a[15]')

class GenrePageLocators(BasePageLocators):
    OPEN_ALL  = (By.XPATH, '//*[@id="root"]/div[4]')
    SPORT = (By.XPATH, '//*[@id="root"]/div[3]/a[15]')

  