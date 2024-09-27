import pytest
from selenium import webdriver

from pages.base_page import BasePage


@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture
def base_page(browser):
    return BasePage(browser)


@pytest.fixture
def clear_results_file():
    with open("results.txt", "w") as f:
        f.write("")
