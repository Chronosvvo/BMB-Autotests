from playwright.sync_api import Page, expect
import config.urls as urls


def test_navigation_logo_header(homepage: Page) -> None:
    homepage.get_by_test_id("header-logo").click()

    expect(homepage).to_have_url("/ru")

def test_navigation_video_header(homepage):
    homepage.get_by_test_id("header-nav-videos").click()

    expect(homepage.locator("#videos")).to_be_visible()

def test_navigation_repertoire_header(homepage):
    homepage.get_by_test_id("header-nav-repertoire").click()

    expect(homepage).to_have_url(urls.repertoire_url)

def test_navigation_reviews_header(homepage):
    homepage.get_by_test_id("header-nav-reviews").click()

    expect(homepage.locator("#reviews")).to_be_visible()

def test_navigation_contacts_header(homepage):
    homepage.get_by_test_id("header-nav-contact").click()

    expect(homepage.locator("#contact")).to_be_visible()

def test_navigation_buy_ticket_button_header(homepage):
    with homepage.context.expect_page() as buy_ticket_page:
        homepage.get_by_test_id("header-buy-ticket").click()

    expect(buy_ticket_page.value).to_have_url(urls.buy_ticket_url)

def test_navigation_whatsapp_button_header(homepage):
    with homepage.context.expect_page() as whatsapp_page:
        homepage.get_by_test_id("header-whatsapp").click()

    expect(whatsapp_page.value).to_have_url(urls.whatsapp_url_blank)

def test_navigation_riders_page_footer(homepage):
    homepage.get_by_test_id("footer-riders").click()

    expect(homepage).to_have_url(urls.riders_url)