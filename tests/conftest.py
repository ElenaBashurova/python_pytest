import pytest

from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_url(request):
    browser.config.base_url = 'https://github.com/'


@pytest.fixture(params=[(1920, 1080), (1280, 720)])
def browser_desktop(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(800, 480), (480, 360)])
def browser_mobile(request):
    width, height = request.param
    browser.config.window_width = width
    browser.config.window_height = height


@pytest.fixture(params=[(1920, 1080), (1280, 720), (800, 480), (480, 360)])
def screen_browser(request):
    resolution = request.param
    width, height = resolution
    browser.config.window_width = width
    browser.config.window_height = height
    if resolution in [(1920, 1080), (1280, 720)]:
        return True
    else:
        return False