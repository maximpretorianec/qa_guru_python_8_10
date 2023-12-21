import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_launch():
    browser.driver.set_window_size(1920, 1080)
    browser.open('https://demoqa.com/automation-practice-form')
    yield
    browser.quit()
