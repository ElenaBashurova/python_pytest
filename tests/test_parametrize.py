import pytest
from selene import browser, have


@pytest.mark.parametrize("browser_desktop", [(1920, 1080), (1280, 720)], indirect=True)
def test_desktop(browser_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[for="login_field"]').should(have.text('Username or email address'))


@pytest.mark.parametrize("browser_mobile", [(800, 480), (480, 360)], indirect=True)
def test_mobile(browser_mobile):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[for="login_field"]').should(have.text('Username or email address'))