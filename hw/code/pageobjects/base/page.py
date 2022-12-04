from urllib.parse import urljoin


class Page(object):
    BASE_URL = 'https://planexa.ru/'

    def __init__(self, driver):
        self.driver = driver 

    def open(self, path):
        url = urljoin(self.BASE_URL, path)
        self.driver.get(url)
        self.driver.maximize_window()
