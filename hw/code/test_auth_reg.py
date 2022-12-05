import pytest
from pages.auth import AuthPage
import random

LOGIN_EXISTS = 'test'
BADLOGIN = 'тест'
MAX_LENGTH = 45


def get_register(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    return auth_page.go_to_register()


def test_register_error_empty(browser):
    register_page = get_register(browser)
    kwargs = dict([(key, 'test') for key in register_page.data.keys()])
    for field, func in register_page.data.items():
        kw_new = kwargs.copy()
        kw_new[field] = ''
        register_page.register(**kw_new)
        assert func() is True
        assert len(register_page.get_error_messages()) == (2 if field in ['password', 'confirm_password'] else 1)


def test_register_error_long(browser):
    register_page = get_register(browser)
    kwargs = dict([(key, 'test') for key in register_page.data.keys()])
    for field, func in register_page.data.items():
        kw_new = kwargs.copy()
        kw_new[field] = 'a' * (MAX_LENGTH + 1)
        register_page.register(**kw_new)
        assert func() is True
        assert len(register_page.get_error_messages()) == (2 if field in ['password', 'confirm_password'] else 1)


def test_register_error_exists(browser):
    register_page = get_register(browser)
    register_page.register('test', 'test', LOGIN_EXISTS, 'test', 'test')
    assert register_page.is_login_error() is True
    assert len(register_page.get_error_messages()) == 1


def test_register_error_badlogin(browser):
    register_page = get_register(browser)
    register_page.register('test', 'test', BADLOGIN, 'test', 'test')
    assert register_page.is_login_error() is True
    assert len(register_page.get_error_messages()) == 1


def test_register_error_nopasswmatch(browser):
    register_page = get_register(browser)
    register_page.register('test', 'test', 'test', 'test', 'test1')
    assert register_page.is_password_error() is True
    assert register_page.is_confirm_password_error() is True
    assert len(register_page.get_error_messages()) == 2


def test_register_cancel(browser):
    register_page = get_register(browser)
    register_page.go_back() # все assert'ы уже внутри метода


def test_register_success(browser):
    register_page = get_register(browser)
    while True:
        login = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz1234567890", k=10))
        pytest.login = login
        pytest.password = "test"
        register_page.register("test", "test", pytest.login, pytest.password, pytest.password)
        if not register_page.is_login_error():
            break
    assert register_page.is_password_error() is False
    assert register_page.is_confirm_password_error() is False
    assert register_page.get_error_messages() == []
    assert register_page.is_redirected() is True
    register_page.driver.delete_all_cookies()


def test_auth_error_empty(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login('', '')
    assert auth_page.is_login_error() is True
    assert auth_page.is_password_error() is True
    assert len(auth_page.get_error_messages()) == 2


def test_auth_error_badpair(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login('test', 'testingtesting')
    assert len(auth_page.get_error_messages()) == 2


def test_auth_error_long(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login('normal', 'a' * (MAX_LENGTH + 1))
    assert auth_page.is_login_error() is False
    assert auth_page.is_password_error() is True
    assert len(auth_page.get_error_messages()) == 1


def test_auth_error_badlogin(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(BADLOGIN, 'test')
    assert auth_page.is_login_error() is True
    assert auth_page.is_password_error() is False
    assert len(auth_page.get_error_messages()) == 1


def test_auth_redirect(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    register_page = auth_page.go_to_register()
    assert register_page.is_loaded() is True


def test_auth_success(browser):
    auth_page = AuthPage(browser)
    auth_page.go_to_site()
    auth_page.login(pytest.login, pytest.password)
    assert auth_page.is_login_error() is False
    assert auth_page.is_password_error() is False
    assert auth_page.get_error_messages() == []
    assert auth_page.is_redirected() is True
    auth_page.driver.delete_all_cookies()
