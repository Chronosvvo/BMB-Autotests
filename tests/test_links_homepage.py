from importlib import import_module
from playwright.sync_api import Page, expect
import config.urls as urls
import pytest
from pages.components import header, footer
from pages import home_page

@pytest.mark.smoke
@pytest.mark.p0
def test_buy_ticket_link(page_ru: Page) -> None:
    header_page = header.Header(page_ru)

    expect(header_page.buy_ticket_button).to_have_attribute("href", urls.buy_ticket_url)
    expect(header_page.buy_ticket_button_mobile).to_have_attribute("href", urls.buy_ticket_url)

@pytest.mark.smoke
@pytest.mark.p2
def test_whatsapp_link(page_ru: Page) -> None:
    header_page = header.Header(page_ru)
    footer_page = footer.Footer(page_ru)
    main_page = home_page.MainPage(page_ru)

    expect(header_page.whatsapp_button_header).to_have_attribute("href", urls.whatsapp_url)
    expect(main_page.whatsapp_hero_button).to_have_attribute("href", urls.whatsapp_url)
    expect(main_page.whatsapp_floating_button).to_have_attribute("href", urls.whatsapp_url)
    expect(main_page.whatsapp_button_in_contact_form).to_have_attribute("href", urls.whatsapp_url)
    expect(footer_page.whatsapp_footer_link).to_have_attribute("href", urls.whatsapp_url)

@pytest.mark.smoke
@pytest.mark.p2
def test_phone_link(page_ru: Page) -> None:
    main_page = home_page.MainPage(page_ru)
    footer_page = footer.Footer(page_ru)

    expect(main_page.phone_link_hero).to_have_attribute("href", urls.phone_url)
    expect(main_page.phone_link_in_contact_form).to_have_attribute("href", urls.phone_url)
    expect(footer_page.phone_number_footer_link).to_have_attribute("href", urls.phone_url)

@pytest.mark.smoke
@pytest.mark.p2
def test_youtube_link(page_ru: Page) -> None:

    expect(page_ru.get_by_test_id("videos-youtube-cta")).to_have_attribute("href", urls.youtube_url)

@pytest.mark.smoke
@pytest.mark.p2
def test_repertoire_link(page_ru: Page) -> None:

    expect(page_ru.get_by_test_id("repertoire-preview-cta")).to_have_attribute("href", urls.repertoire_url)
