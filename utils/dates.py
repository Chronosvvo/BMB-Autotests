from datetime import date


DAYS_RU = [
    "понедельник",
    "вторник",
    "среда",
    "четверг",
    "пятница",
    "суббота",
    "воскресенье",
]

MONTHS_RU = [
    "января",
    "февраля",
    "марта",
    "апреля",
    "мая",
    "июня",
    "июля",
    "августа",
    "сентября",
    "октября",
    "ноября",
    "декабря",
]


def date_to_calendar_label(value: date) -> str:
    return (
        f"{DAYS_RU[value.weekday()]}, "
        f"{value.day} "
        f"{MONTHS_RU[value.month - 1]} "
        f"{value.year} г."
    )