import pytest
from selene import browser, have


@pytest.mark.desktop
def test_desktop(screen_browser):
    if not screen_browser:
        pytest.skip(reason='Неопределенный формат для экрана компьютера')
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[for="login_field"]').should(have.text('Username or email address'))


@pytest.mark.mobile
def test_mobile(screen_browser):
    if screen_browser:
        pytest.skip(reason='Неопределенный формат экрана телефона')
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[for="login_field"]').should(have.text('Username or email address'))