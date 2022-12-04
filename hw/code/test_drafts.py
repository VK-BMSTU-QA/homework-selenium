import os

from pages.auth import AuthPage
from pages.drafts import DraftPage
from pages.drafts import Draft
from dotenv import load_dotenv

load_dotenv()  # LOGIN and PASSWORD


SAMPLE_DRAFT = Draft('1 test address', '1 test theme', '1 test text')
SAMPLE_DRAFT_LONGTHEME = Draft('1 test address', '1 test long long long long long long long long long theme',
                               '1 test text')
SAMPLE_DRAFT_LONGADDRESS = Draft('1 test long long long long long long long long long address', '1 test theme',
                                 '1 test text')
SAMPLE_DRAFT_UPDATED = Draft('1 test address updated', '1 test theme updated', '1 test text updated')


def test_create_draft_success(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_count = draft_page.list_count()
    draft_page.create_draft(SAMPLE_DRAFT)
    assert draft_count + 1 == draft_page.list_count()


def test_create_draft_error_longtheme(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_count = draft_page.list_count()
    draft_page.create_draft(SAMPLE_DRAFT_LONGTHEME)
    assert draft_count == draft_page.list_count()


def test_create_draft_error_longaddress(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_count = draft_page.list_count()
    draft_page.create_draft(SAMPLE_DRAFT_LONGADDRESS)
    assert draft_count == draft_page.list_count()


def test_create_draft_cancel(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_count = draft_page.list_count()
    draft_page.create_draft(SAMPLE_DRAFT, cancel=True)
    assert draft_count == draft_page.list_count()


def test_show_draft_list(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_count = draft_page.list_count()
    draft_page.create_draft(SAMPLE_DRAFT)
    draft_page.create_draft(SAMPLE_DRAFT)
    draft_page.create_draft(SAMPLE_DRAFT)
    draft_page.go_to_site()
    assert draft_count + 3 == draft_page.list_count()


def test_delete_draft(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_page.create_draft(SAMPLE_DRAFT)
    assert draft_page.list_count() > 0
    draft_page.delete_all()
    assert draft_page.list_count() == 0


def test_show_draft(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_page.delete_all()
    draft_page.create_draft(SAMPLE_DRAFT)
    draft_page.open_draft(index=0)
    opened_draft = draft_page.get_draft_value()
    assert opened_draft.address == SAMPLE_DRAFT.address
    assert opened_draft.theme == SAMPLE_DRAFT.theme
    assert opened_draft.text == SAMPLE_DRAFT.text


def test_update_draft(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(os.getenv('LOGIN'), os.getenv('PASSWORD'))

    draft_page = DraftPage(browser)
    draft_page.go_to_site()
    draft_page.delete_all()
    draft_page.create_draft(SAMPLE_DRAFT)

    draft_page.open_draft(index=0)
    draft_page.update_draft(SAMPLE_DRAFT_UPDATED)

    draft_page.open_draft(index=0)
    updated_draft = draft_page.get_draft_value()

    assert updated_draft.address == SAMPLE_DRAFT_UPDATED.address
    assert updated_draft.theme == SAMPLE_DRAFT_UPDATED.theme
    assert updated_draft.text == SAMPLE_DRAFT_UPDATED.text
