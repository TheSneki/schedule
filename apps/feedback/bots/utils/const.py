from enum import Enum


class Messengers(Enum):
    VK = "VK"
    TELEGRAM = "TELGRAM"


class Commands(Enum):
    ECHO = "ECHO"
    GET_EDUCATIONAL_LEVELS = "GET_EDUCATIONAL_LEVELS"
    GET_GROUPS_BY_EDUCATIONAL_LEVEL = "GET_GROUPS_BY_EDUCATIONAL_LEVEL"


VK_MAX_BUTTONS_IN_KEYBOARD = 40


MAIN_MENU_KEYBOARD_LAYOUT = [
    "Выбор группы",
    "Настройки",
    "Статус"
]
assert len(MAIN_MENU_KEYBOARD_LAYOUT) <= VK_MAX_BUTTONS_IN_KEYBOARD, \
    f"Keyboards can't have more than {VK_MAX_BUTTONS_IN_KEYBOARD} buttons"
