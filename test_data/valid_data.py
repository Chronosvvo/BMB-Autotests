VALID_NAMES = [
    "Ан",                  # минимум 2 символа
    "Валерий",             # кириллица
    "Valerii",             # латиница
    "Иван Петров",         # пробел
    "Анна-Мария",          # дефис
    "O'Connor",            # апостроф
    "Jean-Pierre",         # латиница + дефис
    "Мария Иванова",       # кириллица + пробел
    "Алексей O'Connor",    # кириллица + латиница + апостроф
    "Jean Pierre-Smith",    # пробел + дефис
    "A" * 50,
    "B" * 51,
    "C" * 49
]

#В поле есть фильтрация по вводу, поэтому при вводе этих данных лишнее удаляется и номер становится валидным
VALID_PHONES = [
    "+994501234567",       # Azerbaijan
    "+994551234567",       # Azerbaijan
    "+12025550123",        # USA
    "+442071838750",       # UK
    "+4915123456789",      # Germany
    "+33142345678",        # France
    "994501234567",        # нет +
    "++994501234567",      # два +
    " +994501234567",      # пробел перед +
    "+994501234567 ",      # пробел после номера
]


VALID_EMAILS = [
    "test@example.com",                  # базовый вариант
    "user123@example.com",               # цифры в local-part
    "user.name@example.com",             # точка
    "user-name@example.com",             # дефис
    "user_name@example.com",             # underscore допустим в local-part
    "user+tag@example.com",              # plus addressing
    "first.last@example.az",             # .az
    "test@example.org",                 # .org
    "user123@test-domain.com",           # дефис в домене
    "a@example.com",                      # короткая local-part
    "a" * 63 + "@" + "q" * 186 + ".com",
    "b" * 64 + "@domain.com",

]