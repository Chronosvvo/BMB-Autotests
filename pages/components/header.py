from playwright.sync_api import Page, Locator

from config.urls import repertoire_url


class Header:
    def __init__(self, page):
        self.page = page

        # лого
        self.logo_button = self.page.get_by_test_id("header-logo")
        # меню видео
        self.video_menu_button = self.page.get_by_test_id("header-nav-videos")
        # меню репертуар
        self.repertoire_menu_button = self.page.get_by_test_id("header-nav-repertoire")
        # меню отзывы
        self.reviews_menu_button =  self.page.get_by_test_id("header-nav-reviews")
        # меню контакты
        self.contacts_menu_button = self.page.get_by_test_id("header-nav-contact")
        # ru
        self.ru_lang_button =  self.page.get_by_test_id("header-lang-ru")
        # en
        self.en_lang_button = self.page.get_by_test_id("header-lang-en")
        # az
        self.az_lang_button =  self.page.get_by_test_id("header-lang-az")
        # Кнопка "купить билет"
        self.buy_ticket_button = self.page.get_by_test_id("header-buy-ticket")
        # Вотсап
        self.whatsapp_button_header = self.page.get_by_test_id("header-whatsapp")





    def logo_header_click(self):
        self.logo_button.click()


    def buy_ticket_button_click(self):
        with self.page.context.expect_page() as buy_ticket_page:
            self.buy_ticket_button.click()

        return buy_ticket_page.value

    def whatsapp_button_header_click(self):
        with self.page.context.expect_page() as whatsapp_page:
            self.whatsapp_button_header.click()

        return whatsapp_page.value