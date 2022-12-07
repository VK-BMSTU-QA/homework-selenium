import pytest
from ui.pages.base_page import BasePage
from ui.base_case import BaseCase


class TestSearchClick(BaseCase):
    authorize = True
    button_search = BasePage.locators.BUTTON_SEARCH
    button_search_close = BasePage.locators.BUTTON_CLOSE_SEARCH
    search = BasePage.locators.INPUT_SEARCH

    def test_search_open_clicking(self):
        self.base_page.click(self.button_search, 20)
        search = (self.base_page.driver.find_elements_by_xpath(self.search[1])[0])
        assert search.get_attribute('hidden') is None
        self.base_page.click(self.button_search_close, 20)

    def test_search_close_clicking(self):
        self.base_page.click(self.button_search, 20)
        self.base_page.click(self.button_search_close, 20)
        search = (self.base_page.driver.find_elements_by_xpath(self.search[1])[0])
        assert search.get_attribute('hidden') is not None


class TestSearchData(BaseCase):
    authorize = True
    button_search = BasePage.locators.BUTTON_SEARCH
    button_search_close = BasePage.locators.BUTTON_CLOSE_SEARCH
    search = BasePage.locators.INPUT_SEARCH

    @pytest.mark.parametrize("content, expected", [
        (
                'Аватар',
                'Фильмы'
        ),
        (
                'Шерлок',
                'Сериалы'
        ),
        (
                'Хью Лори',
                'Персоны'
        ),

    ])
    def test_search_categories(self, content, expected):
        self.base_page.click(self.button_search, 20)
        search = (self.base_page.driver.find_elements_by_xpath(self.search[1])[0])
        search.send_keys(content)
        topic = self.base_page.wait_visability_of_elem(self.base_page.locators.TOPIC)
        title_topic = self.base_page.wait_visability_of_elem(self.base_page.locators.TITLE_TOPIC)
        res_topic = self.base_page.wait_visability_of_elem(self.base_page.locators.RES_TOPIC)
        assert topic is not None
        assert title_topic.text == expected
        assert res_topic.text == content
        self.base_page.click(self.button_search_close, 20)


class TestSearchEmptyData(BaseCase):
    authorize = True
    button_search = BasePage.locators.BUTTON_SEARCH
    button_search_close = BasePage.locators.BUTTON_CLOSE_SEARCH
    search = BasePage.locators.INPUT_SEARCH
    content = 'фильм/сериал/персона которого нет в базе'
    expected = 'Ничего не найдено'

    def test_search_empty(self):
        self.base_page.click(self.button_search, 20)
        search = (self.base_page.driver.find_elements_by_xpath(self.search[1])[0])
        search.send_keys(self.content)
        title_topic = self.base_page.wait_visability_of_elem(self.base_page.locators.EMPTY_TOPIC)
        assert title_topic.text == self.expected
        self.base_page.click(self.button_search_close, 20)


class TestSearchPartData(BaseCase):
    authorize = True
    button_search = BasePage.locators.BUTTON_SEARCH
    button_search_close = BasePage.locators.BUTTON_CLOSE_SEARCH
    search = BasePage.locators.INPUT_SEARCH
    content = 'ав'
    expected = ['Аватар', 'Гравити Фолз', 'Джон Фавро', 'Сиэра Браво']

    def test_search_categories(self):
        self.base_page.click(self.button_search, 20)
        search = (self.base_page.driver.find_elements_by_xpath(self.search[1])[0])
        search.send_keys(self.content)
        res_topic = self.base_page.find_all_elemets(self.base_page.locators.RES_TOPICS)
        for i in range(1, len(self.expected)):
            assert res_topic[i].text == self.expected[i]
