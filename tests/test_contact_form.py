from playwright.sync_api import Page, expect


from utils.dates import date_to_calendar_label
from datetime import date, timedelta
import pytest
from pages.home_page import MainPage
from test_data.valid_data import VALID_NAMES
from test_data.invalid_data import INVALID_NAMES
from test_data.valid_data import VALID_EMAILS
from test_data.invalid_data import INVALID_EMAILS
from test_data.valid_data import VALID_PHONES
from test_data.invalid_data import INVALID_PHONES


@pytest.mark.smoke
@pytest.mark.p0
def test_contact_form_is_visible(page_ru):
    bmb_main_page = MainPage(page_ru)
    expect(bmb_main_page.contact_form).to_be_visible()

@pytest.mark.regression
@pytest.mark.p1
def test_contact_form_required_fields_are_visible(page_ru):
    bmb_main_page = MainPage(page_ru)
    expect(bmb_main_page.contact_name_input).to_be_visible()
    expect(bmb_main_page.contact_email_input).to_be_visible()
    expect(bmb_main_page.contact_phone_input).to_be_visible()
    expect(bmb_main_page.contact_submit_button).to_be_visible()

@pytest.mark.regression
@pytest.mark.p3
def test_contact_form_required_fields_are_marked(page_ru):
    bmb_main_page = MainPage(page_ru)

    expect(bmb_main_page.contact_name_input).to_have_attribute("aria-required", "true")
    expect(bmb_main_page.contact_email_input).to_have_attribute("aria-required", "true")
    expect(bmb_main_page.contact_phone_input).to_have_attribute("aria-required", "true")


@pytest.mark.smoke
@pytest.mark.p1
def test_contact_form_empty_with_submit_button(page_ru):
    bmb_main_page = MainPage(page_ru)

    bmb_main_page.submit_button_click()

    expect(bmb_main_page.contact_name_input).to_have_attribute("aria-invalid", "true")
    expect(bmb_main_page.contact_error_name).to_have_attribute("role", "alert")

    expect(bmb_main_page.contact_phone_input).to_have_attribute("aria-invalid", "true")
    expect(bmb_main_page.contact_error_phone).to_have_attribute("role", "alert")

    expect(bmb_main_page.contact_email_input).to_have_attribute("aria-invalid", "true")
    expect(bmb_main_page.contact_error_email).to_have_attribute("role", "alert")


# Тест валидных данных в поле Имя
@pytest.mark.regression
@pytest.mark.p3
@pytest.mark.parametrize("name", VALID_NAMES)
def test_valid_name(page_ru, name):
    bmb_main_page = MainPage(page_ru)

    bmb_main_page.fill_name(name)

    bmb_main_page.submit_button_click()

    assert not bmb_main_page.contact_error_name.is_visible()

# Тест невалидных данных в поле Имя
@pytest.mark.regression
@pytest.mark.p3
@pytest.mark.parametrize("name", INVALID_NAMES)
def test_invalid_name(page_ru, name):
    bmb_main_page = MainPage(page_ru)

    bmb_main_page.fill_name(name)

    bmb_main_page.submit_button_click()

    assert bmb_main_page.contact_error_name.is_visible()

# Тест валидных данных в поле Телефон
@pytest.mark.regression
@pytest.mark.p3
@pytest.mark.parametrize("phone", VALID_PHONES)
def test_valid_phone(page_ru, phone):
    bmb_main_page = MainPage(page_ru)
    bmb_main_page.fill_phone(phone)
    bmb_main_page.submit_button_click()

    assert not bmb_main_page.contact_error_phone.is_visible()

# Тест невалидных данных в поле Телефон
@pytest.mark.regression
@pytest.mark.p3
@pytest.mark.parametrize("phone", INVALID_PHONES)
def test_invalid_phone(page_ru, phone):
    bmb_main_page = MainPage(page_ru)
    bmb_main_page.fill_phone(phone)
    bmb_main_page.submit_button_click()

    assert bmb_main_page.contact_error_phone.is_visible()

# Тест валидных данных в поле email
@pytest.mark.regression
@pytest.mark.p3
@pytest.mark.parametrize("email", VALID_EMAILS)
def test_valid_email(page_ru, email):
    bmb_main_page = MainPage(page_ru)
    bmb_main_page.fill_email(email)
    bmb_main_page.submit_button_click()

    assert not bmb_main_page.contact_error_email.is_visible()

# Тест невалидных данных в поле email
@pytest.mark.regression
@pytest.mark.p3
@pytest.mark.parametrize("email", INVALID_EMAILS)
def test_invalid_email(page_ru, email):
    bmb_main_page = MainPage(page_ru)
    bmb_main_page.fill_email(email)
    bmb_main_page.submit_button_click()

    assert bmb_main_page.contact_error_email.is_visible()

@pytest.mark.regression
@pytest.mark.p4
def test_contact_form_message_validation(page_ru):
    bmb_main_page = MainPage(page_ru)
    test_message = "Тестовое сообщение"
    test_message_4000 = "F" * 4000
    test_message_3999 = "A" * 3999
    test_message_4001 = "B" * 4001

    expect(bmb_main_page.contact_message_field_counter).to_contain_text(f"0/4000")

    bmb_main_page.contact_message_input.fill(test_message)
    expect(bmb_main_page.contact_message_field_counter).to_contain_text(f"{len(test_message)}/4000")

    bmb_main_page.contact_message_input.fill(test_message_4000)
    expect(bmb_main_page.contact_message_field_counter).to_contain_text(f"4000/4000")

    bmb_main_page.contact_message_input.fill(test_message_4001)
    expect(bmb_main_page.contact_message_field_counter).to_contain_text("4000/4000")

    bmb_main_page.contact_message_input.fill(test_message_3999)
    expect(bmb_main_page.contact_message_field_counter).to_contain_text(f"3999/4000")


@pytest.mark.regression
@pytest.mark.p3
def test_contact_form_date_picker_is_opened(page_ru):
    bmb_main_page = MainPage(page_ru)


    expect(bmb_main_page.contact_date_trigger).to_have_attribute("aria-expanded", "false")

    bmb_main_page.open_calendar()
    expect(bmb_main_page.contact_date_trigger).to_have_attribute("aria-expanded", "true")

    bmb_main_page.open_calendar()
    expect(bmb_main_page.contact_date_trigger).to_have_attribute("aria-expanded", "false")

@pytest.mark.regression
@pytest.mark.p4
def test_contact_date_cannot_be_filled(page_ru: Page) -> None:
    bmb_main_page = MainPage(page_ru)

    expect(bmb_main_page.contact_date_input_loc).to_be_hidden()

@pytest.mark.regression
@pytest.mark.p3
@pytest.mark.parametrize(
    "days_from_today",
    [0, 1, 7, 30, 150]
)

# проверка настоящей и будущих дат
@pytest.mark.regression
@pytest.mark.p2
def test_contact_form_date_picker_choose(page_ru, days_from_today):
    bmb_main_page = MainPage(page_ru)

    today = date.today()
    target_date = today + timedelta(days=days_from_today)

    bmb_main_page.open_calendar()

    month_diff = (target_date.year - today.year) * 12 + (target_date.month - today.month)

    if month_diff > 0:
        for i in range(month_diff):
            bmb_main_page.next_month()

    date_button = page_ru.get_by_role("button", name=date_to_calendar_label(target_date))
    expect(date_button).to_be_enabled()

    date_button.click()

    expect(bmb_main_page.contact_date_input_loc).to_have_value(target_date.isoformat())


@pytest.mark.p3
@pytest.mark.regression
def test_contact_form_event_type(page_ru):
    bmb_main_page = MainPage(page_ru)

    bmb_main_page.open_event_type()

    expect(bmb_main_page.contact_event_type_option).to_be_visible()

    bmb_main_page.open_event_type()
    expect(bmb_main_page.contact_event_type_option).not_to_be_visible()

@pytest.mark.regression
@pytest.mark.p3
@pytest.mark.parametrize(
    "event_type", [
        "Корпоратив",
        "Свадьба",
        "Фестиваль",
        "Частное событие",
        "Концерт"
    ]
)
# Проверка выбора каждого элемента
def test_contact_form_choose_event_type(page_ru, event_type):
    bmb_main_page = MainPage(page_ru)

    bmb_main_page.open_event_type()

    bmb_main_page.select_event_type(event_type)

    expect(bmb_main_page.contact_event_type_trigger).to_contain_text(event_type)

@pytest.mark.smoke
@pytest.mark.p0
def test_send_full_valid_data_contact_form(page_ru, ):
    bmb_main_page = MainPage(page_ru)

    bmb_main_page.fill_name("Тест BMB Имя")
    bmb_main_page.fill_email("test_bmb_email@bmb.band")
    bmb_main_page.fill_phone("+994568541235")
    bmb_main_page.open_event_type()
    bmb_main_page.select_event_type("Свадьба")
    bmb_main_page.open_calendar()
    bmb_main_page.select_date(date.today())
    bmb_main_page.fill_message("Тестовое сообщение, которое отправлено при прохождении Smoke теста")

    with page_ru.expect_response(
        lambda responce: "_serverFn/" in responce.url
    ) as response_info:
        bmb_main_page.submit_button_click()

    response = response_info.value

    assert response.status == 200

    expect(bmb_main_page.success_send_contact_form).to_be_visible()




