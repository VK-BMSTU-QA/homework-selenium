import pytest
from ui.paths import paths
from ui.components.search_page import SearchPage
from ui.base_case.base_case import BaseCase


class TestSearch(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = SearchPage(driver, url_config)

    restaurant_name = "Guava bar"
    category_name = "Суши"
    MAX_LENGTH_QUERY = 101
    TOO_LONG_QUERY = "q" * MAX_LENGTH_QUERY
    NON_EXISTENT_QUERY = "ъъъъъъъъъ"
    GUAVA_BAR_EXTRA_SPACE = "Guava   bar"
    GUAVA_BAR_WRONG_CASE = "gUAVA bar"
    EMPY = ""
    SPACES = "   "

    @pytest.mark.parametrize(
        "query,expected_restaurant",
        [
            (restaurant_name, restaurant_name),
            (GUAVA_BAR_WRONG_CASE, restaurant_name),
            (GUAVA_BAR_EXTRA_SPACE, restaurant_name),
        ],
    )
    def test_search_restaurant(self, query, expected_restaurant):
        self.page.search_with_result(query)
        assert self.page.is_first_result(expected_restaurant)

    @pytest.mark.parametrize(
        "query",
        [
            (EMPY),
            (SPACES),
        ],
    )
    def test_search_restaurant_empty_query(self, query):
        self.page.search_with_result(query)
        assert self.page.is_url_matches(paths.MAIN)

    def test_nonexistent_query(self):
        self.page.search_with_result(self.NON_EXISTENT_QUERY)
        assert self.page.have_nothing_found()

    def test_too_long_query(self):
        self.page.search_wrong(self.TOO_LONG_QUERY)
        assert self.page.is_query_too_long()

    def test_category_search(self):
        self.page.search_with_result(self.category_name)
        assert self.page.has_results()
