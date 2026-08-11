NAME_BOUNDARIES = [
    "A",                  # 1, invalid
    "AB",                 # 2, valid
    "A" * 49,             # 49, valid
    "A" * 50,             # 50, valid
    "A" * 51,             # 51, invalid
]