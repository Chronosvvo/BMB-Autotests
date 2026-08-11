from importlib import import_module

from playwright.sync_api import Page, expect
import config.urls as urls


def test_buy_ticket_link(homepage: Page) -> None:


    expect(homepage.get_by_test_id("header-buy-ticket")).to_have_attribute("href", urls.buy_ticket_url)

    expect(homepage.get_by_test_id("header-buy-ticket-mobile")).to_have_attribute("href", urls.buy_ticket_url)


def test_whatsapp_link(homepage: Page) -> None:


    expect(homepage.get_by_test_id("header-whatsapp")).to_have_attribute("href", urls.whatsapp_url)

    expect(homepage.get_by_test_id("hero-whatsapp")).to_have_attribute("href", urls.whatsapp_url)

    expect(homepage.get_by_test_id("floating-whatsapp")).to_have_attribute("href", urls.whatsapp_url)

    expect(homepage.get_by_test_id("contact-whatsapp")).to_have_attribute("href", urls.whatsapp_url)

    expect(homepage.get_by_test_id("footer-whatsapp")).to_have_attribute("href", urls.whatsapp_url)

def test_phone_link(homepage: Page) -> None:


    expect(homepage.get_by_test_id("hero-call")).to_have_attribute("href", urls.phone_url)

    expect(homepage.get_by_test_id("contact-call")).to_have_attribute("href", urls.phone_url)

    expect(homepage.get_by_test_id("footer-phone")).to_have_attribute("href", urls.phone_url)

def test_youtube_link(homepage: Page) -> None:


    expect(homepage.get_by_test_id("videos-youtube-cta")).to_have_attribute("href", urls.youtube_url)

def test_repertoire_link(homepage: Page) -> None:


    expect(homepage.get_by_test_id("repertoire-preview-cta")).to_have_attribute("href", urls.repertoire_url)

def test_riders_link(homepage: Page) -> None:


    expect(homepage.get_by_test_id("footer-riders")).to_have_attribute("href", urls.riders_url)
