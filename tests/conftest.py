import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_launch():
    browser.driver.set_window_size(1920, 1080)
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()
