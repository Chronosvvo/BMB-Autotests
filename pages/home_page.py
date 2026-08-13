from playwright.sync_api import Page



class MainPage():
    BASE_URL = "https://dev.bmb.az/ru"

    def __init__(self, page):
        self.page = page


        self.hero_block = self.page.get_by_test_id("main")

        # форма обратной связи
        self.contact_form = self.page.get_by_test_id("contact-form")

        # поле Имя
        self.contact_name_input = self.contact_form.get_by_test_id("contact-input-name")

        # поле Телефон
        self.contact_phone_input = self.contact_form.get_by_test_id("contact-input-phone")

        # поле почты
        self.contact_email_input = self.contact_form.get_by_test_id("contact-input-email")

        # поле даты
        self.contact_date_trigger = self.contact_form.get_by_test_id("contact-date-trigger")

        # поповер календаря
        self.contact_date_popover = self.page.get_by_test_id("contact-date-popover")

        # кнопка выбора предыдущего месяца
        self.contact_date_prev = self.contact_date_popover.get_by_test_id("contact-date-prev")

        # Кнопка выбора месяца и года
        self.contact_date_month_toggle = self.contact_date_popover.get_by_test_id("contact-date-view-toggle")

        # кнопка выбора следующего месяца
        self.contact_date_next = self.contact_date_popover.get_by_test_id("contact-date-next")

        # ввод сообщение
        self.contact_message_input = self.contact_form.get_by_test_id("contact-input-message")

        # открыть выбор типа мероприятия
        self.contact_event_type_trigger = self.contact_form.get_by_test_id("contact-eventType-trigger")

        # выбор типа мероприятия
        self.contact_event_type_option = self.page.get_by_test_id("contact-eventType-options")

        # поле с текстов выбранного event type
        self.contact_event_type_input = self.contact_event_type_trigger.get_by_test_id("contact-input-eventType")

        # кнопка отправки формы
        self.contact_submit_button = self.contact_form.get_by_test_id("contact-submit")

        # аллерт ошибки ввода в поле Имя
        self.contact_error_name = self.contact_form.get_by_test_id("contact-error-name")

        # аллерт ошибки ввода в поле email
        self.contact_error_email = self.contact_form.get_by_test_id("contact-error-email")

        # аллерт ошибки ввода телефона
        self.contact_error_phone = self.contact_form.get_by_test_id("contact-error-phone")

        # поле отображения счетчика символов сообщения
        self.contact_message_field_counter = self.contact_form.get_by_test_id("contact-field-message")

        # локатор input date
        self.contact_date_input_loc = self.contact_form.get_by_test_id("contact-input-date")

        # успешная отправка формы
        self.success_send_contact_form = self.page.get_by_test_id("contact-success")

        # кнопка вотсап в контактной форме
        self.whatsapp_button_in_contact_form = self.page.get_by_test_id("contact-whatsapp")

        # кнопка вотсап в блоке hero
        self.whatsapp_hero_button = self.page.get_by_test_id("hero-whatsapp")

        # floating кнопка вотсап
        self.whatsapp_floating_button = self.page.get_by_test_id("floating-whatsapp")

        # кнопка телефона в блоке hero
        self.phone_link_hero = self.page.get_by_test_id("hero-call")

        # кнопка телефона в контактной форма
        self.phone_link_in_contact_form = self.page.get_by_test_id("contact-call")

        # ссылка на телефон в футере
        self.phone_link_footer = self.page.get_by_test_id("footer-phone")










    # open page
    def open(self):
        self.page.goto(self.BASE_URL)

    def fill_name(self, name):
        self.contact_name_input.fill(name)

    def fill_phone(self, phone):
        self.contact_phone_input.fill(phone)

    def fill_email(self, email):
        self.contact_email_input.fill(email)

    def open_calendar(self):
        self.contact_date_trigger.click()

    def select_date(self, date):
        date_cell = self.contact_date_popover.locator(f'[data-day="{date}"]')
        date_cell.get_by_role("button").click()

    def next_month(self):
        self.contact_date_next.click()
    # получение текста настоящего месяца
    def get_current_month(self):
        return self.contact_date_month_toggle.inner_text()

    def fill_message(self, message):
        self.contact_message_input.fill(message)

    def open_event_type(self):
        self.contact_event_type_trigger.click()

    def select_event_type(self, event_type):
        self.contact_event_type_option.get_by_role("button", name=event_type).click()

    def submit_button_click(self):
        self.contact_submit_button.click()

    def get_selected_date(self):
        return self.contact_date_trigger.inner_text()


