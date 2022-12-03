import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from ui.pages.login import LoginPage
from ui.pages.base_page import BasePage


def get_driver(browser_name):
    if browser_name == "chrome":
        browser = webdriver.Chrome(
            executable_path=ChromeDriverManager().install()
        )
    elif browser_name == "firefox":
        browser = webdriver.Firefox(
            executable_path=GeckoDriverManager().install()
        )
    else:
        raise RuntimeError(f'Unsupported browser: "{browser_name}"')
    browser.maximize_window()
    return browser


@pytest.fixture()
def driver(config):
    browser = config["browser"]
    url = config["url"]

    if browser == "chrome":
        driver = webdriver.Chrome(
            executable_path=ChromeDriverManager().install(), options=Options()
        )
    elif browser == "firefox":
        driver = webdriver.Firefox(
            executable_path=GeckoDriverManager().install()
        )
    else:
        raise RuntimeError(f'Unsupported browser: "{browser}"')

    driver.get(url)
    driver.maximize_window()

    yield driver

    driver.quit()


@pytest.fixture
def base_page(driver):
    return BasePage(driver=driver)


@pytest.fixture(scope="session")
def credentials():
    with open("/home/ilyas/technopark/3semestr/QA/creds", "r") as f:
        login = f.readline().strip()
        password = f.readline().strip()

    return login, password


@pytest.fixture(scope="session")
def cookies(credentials, config):
    driver = get_driver(config["browser"])
    driver.get(config["url"])
    login_page = LoginPage(driver)
    login_page.login(*credentials)
    time.sleep(5)
    cookies = driver.get_cookies()
    print(cookies)
    driver.quit()
    return cookies
