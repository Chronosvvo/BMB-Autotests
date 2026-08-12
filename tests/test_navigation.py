from playwright.sync_api import Page, expect
import config.urls as urls
import pytest
from pages.components import header


@pytest.mark.smoke
def test_navigation_logo_header(homepage: Page) -> None:
    header_page = header.Header(homepage)

    header_page.logo_header_click()
    expect(homepage).to_have_url("/ru")

def test_navigation_video_header(homepage):
    header_page = header.Header(homepage)

    header_page.video_menu_button.click()
    expect(homepage.locator("#videos")).to_be_visible()

def test_navigation_repertoire_header(homepage):
    header_page = header.Header(homepage)

    header_page.repertoire_menu_button.click()
    expect(homepage).to_have_url(urls.repertoire_url)

def test_navigation_reviews_header(homepage):
    header_page = header.Header(homepage)

    header_page.reviews_menu_button.click()
    expect(homepage.locator("#reviews")).to_be_visible()

@pytest.mark.smoke
def test_navigation_contacts_header(homepage):
    header_page = header.Header(homepage)

    header_page.contacts_menu_button.click()
    expect(homepage.locator("#contact")).to_be_visible()

@pytest.mark.smoke
def test_navigation_buy_ticket_button_header(homepage):
    header_page = header.Header(homepage)

    expect(header_page.buy_ticket_button_click()).to_have_url(urls.buy_ticket_url)

@pytest.mark.smoke
def test_navigation_whatsapp_button_header(homepage):
    header_page = header.Header(homepage)

    expect(header_page.whatsapp_button_header_click()).to_have_url(urls.whatsapp_url_blank)

def test_navigation_riders_page_footer(homepage):
    homepage.get_by_test_id("footer-riders").click()

    expect(homepage).to_have_url(urls.riders_url)