from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandObject, CommandStart, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from src.keyboards import inline
from src.utils import states
from src.utils.text import WELCOME_TEXT_1, WELCOME_TEXT_2

configurator_router = Router()


@configurator_router.message(or_f(F.text(text='главное меню'.lower()), CommandStart()))
async def start(message: Message, state: FSMContext):
    """команда /start (Здесь все начинается)"""
    await message.answer(WELCOME_TEXT_1)

    # инициализация клавиатуры
    keyboard = await inline.start_button_keyboard()
    ready_text = await message.answer(WELCOME_TEXT_2, reply_markup=keyboard)

    # Сохраняем идентификатор сообщения для последующего удаления
    await state.set_state(states.Start.start_message_id)
    await state.update_data(start_message_id=ready_text.message_id)