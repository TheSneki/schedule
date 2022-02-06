import enum
from typing import Any, Iterable, List, Union

from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from vkbottle import Keyboard, Text
from vkbottle.tools.dev.keyboard.color import KeyboardButtonColor

from apps.feedback.bots.utils.const import VK_MAX_BUTTONS_IN_KEYBOARD
from apps.timetables.models import Group

from .base import BaseKeyboard
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton


class GroupsKeyboard(BaseKeyboard):
    OFFSET = 2
    ITEMS_PER_PAGE = 8

    def to_vk_api(self) -> Union[str, List[str]]:
        self.data: QuerySet[Group]
        if self.data.count() > VK_MAX_BUTTONS_IN_KEYBOARD:
            self.is_inline = True
            return self._build_multiple_vk_keyboards(self.data)
        return self._build_single_vk_keyboard(self.data)

    def _build_single_vk_keyboard(self, groups: QuerySet[Group]) -> str:
        result = Keyboard(inline=self.is_inline)
        for index, value in enumerate(groups):
            result.add(Text(value.title))
            if (index + 1) % self.OFFSET == 0 and not self._is_last(index, groups):
                result.row()
        if self.has_cancel_button:
            result.row()
            result.add(Text("Главное меню"), KeyboardButtonColor.PRIMARY)
        return result.get_json()

    def _build_multiple_vk_keyboards(self, groups: QuerySet[Group]) -> Iterable[str]:
        paginator = Paginator(groups.order_by("id"), self.ITEMS_PER_PAGE)
        result: List[str] = []
        for index in paginator.page_range:
            page = paginator.page(index)
            result.append(self._build_single_vk_keyboard(page.object_list))
        return result

    def to_telegram_api(self) -> Union[ReplyKeyboardMarkup, List[InlineKeyboardMarkup]]:
        if self.data.count() > VK_MAX_BUTTONS_IN_KEYBOARD:
            self.is_inline = True
            return self._build_multiple_telegram_keyboards()
        return self._build_single_telegram_keyboard(self.data)

    def _build_multiple_telegram_keyboards(self) -> List[InlineKeyboardMarkup]:
        paginator = Paginator(self.data.order_by("id"), self.ITEMS_PER_PAGE)
        result: List[InlineKeyboardMarkup] = []
        for index in paginator.page_range:
            page = paginator.page(index)
            result.append(self._build_single_telegram_keyboard(page.object_list))
        return result

    def _build_single_telegram_keyboard(self, groups: QuerySet[Group]) -> Union[ReplyKeyboardMarkup, InlineKeyboardMarkup]:
        if not self.is_inline:
            result = ReplyKeyboardMarkup(resize_keyboard=True)
            for index, value in enumerate(groups):
                title = value.title
                button = KeyboardButton(title)
                result.add(button)
                if (index + 1) % self.OFFSET == 0 and not self._is_last(index, groups):
                    result.row()
            return result
        buttons = []
        for index, value in enumerate(groups):
            buttons.append(InlineKeyboardButton(text=value.title, callback_data=value.title))
        return InlineKeyboardMarkup(row_width=2).row(*buttons)
