import pytest
from selene import browser, have


@pytest.mark.desktop
def test_desktop_github(browser_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[for="login_field"]').should(have.text('Username or email address'))


@pytest.mark.mobile
def test_mobile_github(browser_mobile):
    browser.open('/')
    browser.element('.Button--link').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('[for="login_field"]').should(have.text('Username or email address'))