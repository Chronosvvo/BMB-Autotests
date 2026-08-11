import pytest
from playwright.sync_api import Page
from pages.home_page import MainPage


@pytest.fixture
def homepage(page: Page) -> Page:
    page.set_viewport_size({"width": 1920, "height": 1080})
    page.goto("/ru")
    return page

@pytest.fixture
def home_page(homepage: MainPage) -> MainPage:
    return MainPage(homepage)