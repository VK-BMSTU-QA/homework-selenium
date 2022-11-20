import pytest
from selenium import webdriver

EXEC_PATH = r"./chromedriver"

@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    #options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path=EXEC_PATH, options=options)
    yield driver
    driver.quit()

def pytest_configure():
    pytest.login = None
    pytest.password = None
