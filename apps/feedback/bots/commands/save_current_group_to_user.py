from typing import Union

from asgiref.sync import sync_to_async

from apps.feedback.bots.utils.const import MAIN_MENU_KEYBOARD_LAYOUT
from apps.feedback.bots.utils.keyboard.main_menu import MainMenuKeyboard
from apps.timetables.usecases.group import get_group_by_title

from .base import CommandWithProfile, MultipleMessages, SingleMessage


class SaveCurrentGroupCommand(CommandWithProfile):

    @property
    def group(self) -> str:
        return self._require_field("group")

    async def _vk_execute(self) -> Union[SingleMessage, MultipleMessages]:
        group = await sync_to_async(get_group_by_title)(self.group)
        await sync_to_async(self.profile.set_group)(group)
        _keyboard = MainMenuKeyboard(MAIN_MENU_KEYBOARD_LAYOUT)
        keyboard_data = _keyboard.to_vk_api()
        return SingleMessage(
            message="Ваш выбор группы был успешно сохранен", keyboard=keyboard_data
        )