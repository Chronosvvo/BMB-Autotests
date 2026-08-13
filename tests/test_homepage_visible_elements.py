from playwright.sync_api import Page, expect
import pytest
from pages import home_page
from pages.components import header,footer



@pytest.mark.smoke
@pytest.mark.p0
def test_page_ru_opens(page_ru: Page):
    expect(page_ru).to_have_url("/ru")

@pytest.mark.smoke
@pytest.mark.p1
def test_header_visible(page_ru: Page):
    header_page = header.Header(page_ru)

    expect(header_page.header).to_be_visible()
    expect(header_page.logo_button).to_be_visible()
    expect(header_page.ru_lang_button).to_be_visible()
    expect(header_page.en_lang_button).to_be_visible()
    expect(header_page.az_lang_button).to_be_visible()
    expect(header_page.buy_ticket_button).to_be_visible()
    expect(header_page.whatsapp_button_header).to_be_visible()
    expect(header_page.video_menu_button).to_be_visible()
    expect(header_page.repertoire_menu_button).to_be_visible()
    expect(header_page.reviews_menu_button).to_be_visible()
    expect(header_page.contacts_menu_button).to_be_visible()

@pytest.mark.smoke
@pytest.mark.p1
def test_footer_visible(page_ru: Page):
    footer_page = footer.Footer(page_ru)

    expect(footer_page.footer).to_be_visible()
    expect(footer_page.logo_button_footer).to_be_visible()

@pytest.mark.smoke
@pytest.mark.p3
def test_page_ru_main_content(page_ru: Page):
    bmb_main_page = home_page.MainPage(page_ru)
    expect(bmb_main_page.hero_block).to_be_visible()