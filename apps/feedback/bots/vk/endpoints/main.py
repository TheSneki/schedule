from vkbottle.bot import Message

from apps.feedback.bots.commands.get_main_menu import GetMainMenuCommand
from apps.feedback.bots.commands.show_id import ShowIDCommand
from apps.feedback.bots.vk.base import BaseVkBot


def init_endpoints(app: BaseVkBot):
    @app.bot.on.message(text=["Привет", "Покажи мой ID"])
    async def echo(message: Message):
        result = await ShowIDCommand(user_id=message.peer_id).execute()
        await app.send_response(result, message)

    @app.bot.on.message(text=["Начать", "Главное меню"])
    async def get_main_menu(message: Message):
        result = await GetMainMenuCommand().execute()
        await app.bot.state_dispenser.delete(message.peer_id)
        await app.send_response(result, message)
