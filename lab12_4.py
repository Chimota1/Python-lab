from typing import Callable, List, Iterable

def has_uppercase(password: str) -> bool:
    return any(c.isupper() for c in password)


def has_digit(password: str) -> bool:
    return any(c.isdigit() for c in password)


def is_long_enough(password: str) -> bool:
    return len(password) >= 8


def has_special_char(password: str) -> bool:
    special_chars = "!@#$%^&*()"
    return any(c in special_chars for c in password)


def no_spaces(password: str) -> bool:
    return ' ' not in password


PASSWORD_RULES: List[Callable[[str], bool]] = [
    has_uppercase,
    has_digit,
    is_long_enough,
    has_special_char,
    no_spaces,
]


def validate_password(password: str) -> bool:
    return all(rule(password) for rule in PASSWORD_RULES)

print(validate_password("StrongPass1!"))