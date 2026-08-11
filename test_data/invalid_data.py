INVALID_NAMES = [
    "",                  # empty
    "А",                 # < 2
    "   "                 # whitespace
]



INVALID_PHONES = [
    "",                      # пустое
    "+99450123ABC",          # буквы
    "+99450ABC1234",         # буквы
    "+99450@123456",         # спецсимвол
    "+99450#123456",         # спецсимвол
    "+99450_123456",         # underscore
    "+994 50 ABC 12 34"      # буквы
]


INVALID_EMAILS = [
    "",                                  # пустое
    "test",                              # нет @ и домена
    "test@",                             # нет домена
    "@example.com",                      # нет local-part
    "test.example.com",                  # нет @
    "test@@example.com",                 # два @
    "test@@" ,                           # два @
    "test@example",                      # нет TLD
    "test@example.",                     # нет TLD после точки
    "test@.com",                         # домен начинается с точки
    ".test@example.com",                 # local-part начинается с точки
    "test.@example.com",                 # local-part заканчивается точкой
    "te..st@example.com",                # две точки подряд
    "test@example..com",
]