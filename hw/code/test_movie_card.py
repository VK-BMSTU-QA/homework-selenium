import os.path
import time

from selenium.webdriver import ActionChains

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.base_case import BaseCase
from hw.code.ui.pages.series_page import SeriesPage
from hw.code.ui.pages.serial_page import SerialPage

class TestLikeButton(BaseCase):
    authorize = True
    button_locator = BasePage.locators.BUTTON_LIKE


    # @pytest.mark.skip("SKIP")

    def test_like_switching(self):
        time.sleep(3)
        a = self.base_page.driver.find_elements(self.button_locator[0], self.button_locator[1])[0].get_attribute("class").split(" ")
        assert 'active-like' not in str(a)
        self.base_page.click(self.button_locator, 10)
        time.sleep(3)
        a = self.base_page.driver.find_elements(self.button_locator[0], self.button_locator[1])[0].get_attribute("class").split(" ")
        assert 'active-like' in str(a)
        self.base_page.click(self.button_locator, 10)


class TestCard(BaseCase):
    authorize = True
    button_locator = BasePage.locators.CARD
    expected_url = "https://movie-space.ru/movie/"
    # @pytest.mark.skip("SKIP")

    def test_like_switching(self):
        time.sleep(3)
        id_movie = self.base_page.driver.find_elements(self.button_locator[0], self.button_locator[1])[0].get_attribute("id")
        self.base_page.click(self.button_locator, 10)
        time.sleep(3)
        assert str(self.driver.current_url) == (self.expected_url + id_movie)


class TestCardHover(BaseCase):
    authorize = True
    button_locator = BasePage.locators.CARD
    # @pytest.mark.skip("SKIP")

    def test_like_switching(self):
        time.sleep(3)
        element = self.base_page.driver.find_elements(self.button_locator[0], self.button_locator[1])[0]
        styles_before = {
        prop: element.value_of_css_property(prop)
        for prop in ['transform']
        }
        ActionChains(self.driver).move_to_element(element).perform()

        styles_after = {
            prop: element.value_of_css_property(prop)
            for prop in ['transform']
        }
        assert styles_after != styles_before


class TestEpisodeCard(BaseCase):
    authorize = True
    element_locator = SeriesPage.locators.EPISODE_CARD
    expected_url = "https://movie-space.ru/player/"
    # @pytest.mark.skip("SKIP")

    def test_page_switching(self):
        time.sleep(3)
        self.series_page.open()
        self.serial_page.open()
        id_movie = os.path.basename(self.driver.current_url)
        self.base_page.click(self.element_locator, 10)
        assert str(self.driver.current_url) == (self.expected_url + id_movie + "?seas=1&ep=1")
        time.sleep(1)




