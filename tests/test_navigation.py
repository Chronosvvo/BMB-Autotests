from playwright.sync_api import Page, expect
import config.urls as urls
import pytest
from pages.components import header, footer


@pytest.mark.smoke
def test_navigation_logo_header(page_ru: Page) -> None:
    header_page = header.Header(page_ru)

    header_page.logo_header_click()
    expect(page_ru).to_have_url("/ru")

@pytest.mark.regression
@pytest.mark.p3
def test_navigation_video_header(page_ru):
    header_page = header.Header(page_ru)

    header_page.video_menu_button.click()
    expect(page_ru.locator("#videos")).to_be_visible()

@pytest.mark.regression
@pytest.mark.p3
def test_navigation_repertoire_header(page_ru):
    header_page = header.Header(page_ru)

    header_page.repertoire_menu_button.click()
    expect(page_ru).to_have_url(urls.repertoire_url)

@pytest.mark.regression
@pytest.mark.p3
def test_navigation_reviews_header(page_ru):
    header_page = header.Header(page_ru)

    header_page.reviews_menu_button.click()
    expect(page_ru.locator("#reviews")).to_be_visible()

@pytest.mark.smoke
@pytest.mark.p4
def test_navigation_contacts_header(page_ru):
    header_page = header.Header(page_ru)

    header_page.contacts_menu_button.click()
    expect(page_ru.locator("#contact")).to_be_visible()

@pytest.mark.smoke
@pytest.mark.p0
def test_navigation_buy_ticket_button_header(page_ru):
    header_page = header.Header(page_ru)

    expect(header_page.buy_ticket_button_click()).to_have_url(urls.buy_ticket_url)

@pytest.mark.smoke
@pytest.mark.p1
def test_navigation_whatsapp_button_header(page_ru):
    header_page = header.Header(page_ru)

    expect(header_page.whatsapp_button_header_click()).to_have_url(urls.whatsapp_url_blank)

@pytest.mark.smoke
@pytest.mark.p2
def test_navigation_riders_page_footer(page_ru):
    footer_page = footer.Footer(page_ru)

    footer_page.riders_button_footer.click()
    expect(page_ru).to_have_url(urls.riders_url)

@pytest.mark.smoke
@pytest.mark.p3
def test_navigation_logo_footer(page_ru):
    footer_page = footer.Footer(page_ru)

    footer_page.logo_button_footer.click()
    expect(page_ru).to_have_url("/ru")

@pytest.mark.smoke
@pytest.mark.p3
def test_navigation_whatsapp_button_footer(page_ru):
    footer_page = footer.Footer(page_ru)

    expect(footer_page.whatsapp_button_footer_click()).to_have_url(urls.whatsapp_url_blank)

