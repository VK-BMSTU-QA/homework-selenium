import os
import time

from pages.auth import AuthPage
from pages.drafts import DraftPage
from pages.locators.header import HeaderLocators
from dotenv import load_dotenv

load_dotenv()  # LOGIN and PASSWORD


def test_go_to_index(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_page.click(HeaderLocators.LOGO_BUTTON)
    assert draft_page.is_redirected('')


def test_go_to_profile(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.environ.get('LOGIN'), os.environ.get('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_page.click(HeaderLocators.MENU_BUTTON)
    draft_page.click(HeaderLocators.PROFILE_BUTTON)
    assert draft_page.is_redirected('profile')


def test_exit_account(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_page.click(HeaderLocators.MENU_BUTTON)
    draft_page.click(HeaderLocators.EXIT_BUTTON)
    assert draft_page.is_redirected('login')
    draft_page.go_to_site()
    assert draft_page.is_redirected('login')


def test_change_color_theme(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    header_color = draft_page.get_css_property(HeaderLocators.HEADER, 'background-color')
    assert header_color == 'rgba(147, 177, 231, 1)'  # default color
    draft_page.click(HeaderLocators.COLOR_MENU_BUTTON)
    draft_page.click(HeaderLocators.GREEN_BUTTON)

    header_color = draft_page.get_css_property(HeaderLocators.HEADER, 'background-color')
    assert header_color == 'rgba(145, 232, 150, 1)'  # green color
