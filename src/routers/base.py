from aiogram import Bot, F, Router
from aiogram.filters import Command, CommandObject, CommandStart, or_f
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message

from schemas.base import config
from src.keyboards import inline
from src.utils import states
from src.utils.text import WELCOME_TEXT_1, WELCOME_TEXT_2

base_router = Router()


@base_router.callback_query(F.data == 'check_subscription')
async def check_subscription_callback(callback_query: CallbackQuery, bot: Bot, state: FSMContext):
    """Проверка подписки, является продолжением subscription middleware"""
    chat_member = await bot.get_chat_member(f'@{config.CHANNEL_USERNAME}', callback_query.from_user.id)
    if chat_member.status == 'left':
        await callback_query.answer("Вы еще не подписались на канал", show_alert=True)
    else:
        await start(callback_query.message, state)
        await callback_query.answer()


@base_router.message(or_f(F.text(text='главное меню'.lower()), CommandStart()))
async def start(message: Message, state: FSMContext):
    """команда /start (Здесь все начинается)"""
    await message.answer(WELCOME_TEXT_1)

    # инициализация клавиатуры
    keyboard = await inline.start_button_keyboard()
    ready_text = await message.answer(WELCOME_TEXT_2, reply_markup=keyboard)

    # Сохраняем идентификатор сообщения для последующего удаления
    await state.set_state(states.Start.start_message_id)
    await state.update_data(start_message_id=ready_text.message_id)