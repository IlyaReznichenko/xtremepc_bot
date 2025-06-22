from collections.abc import Awaitable, Callable
from typing import Any

from aiogram import BaseMiddleware
from aiogram.types import CallbackQuery, Message

from core.logging import logger
from keyboards import inline
from schemas.base import config


class CheckSubscription(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[Message | CallbackQuery, dict[str, Any]], Awaitable[Any]],
            event: Message | CallbackQuery,
            data: dict[str, Any]
    ) -> Any:
        user_id = event.from_user.id
        chat_member = await event.bot.get_chat_member(f'@{config.CHANNEL_USERNAME}', user_id)

        # инициализация клавиатуры
        keyboard = await inline.subscription_check_keyboard()

        if chat_member.status == 'left':
            if isinstance(event, Message):
                logger.info('___message___')
                await event.answer(
                    f'Приветствую, {event.from_user.first_name}! Если хочешь получить доступ к VPN, <b>Подпишись на канал</b>',
                    reply_markup=keyboard
                )
                return None
            elif isinstance(event, CallbackQuery):
                logger.info('___calback___')
                await event.message.answer(
                    f'Приветствую, {event.from_user.first_name}! Если хочешь получить доступ к VPN, <b>Подпишись на канал</b>',
                    reply_markup=keyboard
                )
                await event.answer()  # Ответить на callback query, чтобы убрать часики
                return None
            return None
        else:
            return await handler(event, data)
