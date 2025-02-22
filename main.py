from aiogram import executor
import logging
from bot_config import dp, bot, admins
from handlers import commands, echo, quiz
from handlers import commands, echo, quiz, FSM_registration, FSM_store

async def on_startup(_):
    for admin in admins:
        if __name__ == '__main__':
         commands.register_handlers(dp)
         quiz.register_handlers(dp)
        FSM_registration.register_handlers_fsm(dp)
        FSM_store.register_handlers_fsm(dp)
        echo.register_handlers(dp)

    logging.basicConfig(level=logging.INFO)