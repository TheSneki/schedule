from typing import Iterable, Union

from apps.feedback.bots.utils.keyboard.base import Button
from apps.feedback.bots.utils.keyboard.settings import SettingsKeyboard
from apps.feedback.const import DEFAULT_DAYS_OFFSET
from apps.feedback.models import Profile

from .base import CommandWithProfile, MultipleMessages, SingleMessage


class GetChangeDaysOffsetInfoCommand(CommandWithProfile):

    async def _vk_execute(self) -> Union[SingleMessage, MultipleMessages]:
        msg = "Здесь ты можешь изменить кол-во дней, "
        msg += "на которое я буду показывать тебе расписание\n\n"
        msg += "Ты можешь выбрать из предложенных в клавиатуре вариантов "
        msg += "или выбрать его самостоятельно\n\n"
        msg += "Для того, чтобы выбрать кол-во дней, напиши: !Получать на <кол-во дней>\n"
        msg += "Писать <> не нужно\n\n"
        msg += f"Сейчас ты получаешь расписание на {self.profile.days_offset} дней"
        layout: Iterable[Button] = await self.build_settings_keyboard_layout(self.profile)
        _keyboard = SettingsKeyboard(layout)
        keyboard = _keyboard.to_vk_api()
        return SingleMessage(
            message=msg,
            keyboard=keyboard
        )

    async def build_settings_keyboard_layout(self, profile: Profile) -> Iterable[Button]:
        result = []
        if not profile.days_offset == DEFAULT_DAYS_OFFSET:
            result.append(Button(title=f"!Получать на {DEFAULT_DAYS_OFFSET}"))
        result.append(Button(title="!Получать на 14"))
        for index in range(6):
            result.append(Button(title=f"!Получать на {index + 1}"))
        return result