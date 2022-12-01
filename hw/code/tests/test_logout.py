import pytest

from ui.paths import paths
from ui.components.logout_component import LogoutComponent
from ui.base_case.base_case import BaseCase


class TestLogout(BaseCase):
    @pytest.fixture(scope="function", autouse=True)
    def set_page(self, driver, url_config):
        self.driver = driver
        self.page = LogoutComponent(driver, url_config)

    @pytest.mark.parametrize(
        "src_path,redirect_path",
        [
            (paths.GUAVA_DISHES, paths.GUAVA_DISHES),
            (paths.PROFILE, paths.MAIN),
        ],
    )
    def test_logout_from_pages(self, authorize, src_path, redirect_path):
        self.page.open_path(src_path)
        self.page.logout()
        assert self.page.is_url_matches(redirect_path)

    def test_logout_from_order_history(self, authorize, order):
        self.page.logout()
        assert self.page.is_url_matches(paths.MAIN)
