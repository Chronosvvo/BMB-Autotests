from playwright.sync_api import Page, expect
import pytest

@pytest.mark.smoke
def test_homepage_opens(homepage: Page):
    expect(homepage).to_have_url("/ru")

@pytest.mark.smoke
def test_header_visible(homepage: Page):
    expect(
        homepage.get_by_test_id("header")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-logo")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-lang-ru")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-lang-en")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-lang-az")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-buy-ticket")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-whatsapp")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-nav-videos")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-nav-repertoire")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-nav-reviews")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("header-nav-contact")
    ).to_be_visible()

@pytest.mark.smoke
def test_footer_visible(homepage: Page):
    expect(
        homepage.get_by_test_id("footer")
    ).to_be_visible()

    expect(
        homepage.get_by_test_id("footer-logo")
    ).to_be_visible()

@pytest.mark.smoke
def test_homepage_main_content(homepage: Page):
    expect(
        homepage.get_by_role("main")
    ).to_be_visible()