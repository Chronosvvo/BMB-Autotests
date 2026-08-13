from playwright.sync_api import Page, Locator

from config.urls import repertoire_url


class Footer:
    def __init__(self, page):
        self.page = page


        self.footer = self.page.get_by_test_id("footer")
        # лого футер
        self.logo_button_footer = self.page.get_by_test_id("footer-logo")
        # футер тэглайн
        self.tag_line_footer = self.page.get_by_test_id("footer-tagline")
        # футер инста
        self.instagram_footer_link = self.page.get_by_test_id("footer-instagram")
        # футер тик ток
        self.tiktok_footer_link = self.page.get_by_test_id("footer-tiktok")
        # whatsapp link
        self.whatsapp_footer_link = self.page.get_by_test_id("footer-whatsapp")
        # phone link
        self.phone_number_footer_link = self.page.get_by_test_id("footer-phone")
        # email link
        self.email_footer_link = self.page.get_by_test_id("footer-email")
        # riders button
        self.riders_button_footer = self.page.get_by_test_id("footer-riders")
        # copyright
        self.copyright_footer = self.page.get_by_test_id("footer-legal")




    def whatsapp_button_footer_click(self):
        with self.page.context.expect_page() as whatsapp_page:
            self.whatsapp_footer_link.click()

        return whatsapp_page.value