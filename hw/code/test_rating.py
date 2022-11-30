import os.path
import time

import pytest
from selenium.webdriver import ActionChains

from hw.code.ui.pages.base_page import BasePage
from hw.code.ui.base_case import BaseCase
from hw.code.ui.pages.series_page import SeriesPage


class TestRating(BaseCase):
    authorize = True
    rating = SeriesPage.locators.RATING
    slider = SeriesPage.locators.SLIDER

    @pytest.mark.parametrize("offset, range, expected_color", [
        (
                100,
                (7, 10),
                'rgba(59, 179, 59, 1)'
        ),
        (
                10,
                (4, 7),
                'rgba(212, 225, 61, 1)'

        ),
        (
                -90,
                (1, 3),
                'rgba(225, 61, 61, 1)'

        ),

    ])
    

    def test_rating_value(self,offset,range,expected_color):
        time.sleep(2)
        self.series_page.open()
        time.sleep(2)
        self.serial_page.open()
        time.sleep(2)
        rating = self.base_page.wait_visability_of_elem(self.rating)
        slider = self.base_page.wait_visability_of_elem(self.slider)
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(offset, 0).release().perform()
        assert range[0] < int(rating.text) < range[1]
        assert rating.value_of_css_property('color') == expected_color

class TestSearchEmptyData(BaseCase):
    authorize = True
    rating = SeriesPage.locators.RATING
    slider = SeriesPage.locators.SLIDER
    expected_value = '–'
    expected_color = 'rgba(255, 255, 255, 1)'
    offset = -150
    

    def test_search_empty(self):
        time.sleep(2)
        self.series_page.open()
        time.sleep(2)
        self.serial_page.open()
        time.sleep(2)
        rating = self.base_page.wait_visability_of_elem(self.rating)
        slider = self.base_page.wait_visability_of_elem(self.slider)
        ActionChains(self.driver).click_and_hold(slider).move_by_offset(self.offset, 0).release().perform()
        assert rating.text == self.expected_value
        assert rating.value_of_css_property('color') == self.expected_color