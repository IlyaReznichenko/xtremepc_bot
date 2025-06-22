from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from src.schemas.base import config


async def subscription_check_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Подписаться', url=config.CHANNEL_LINK)],
            [InlineKeyboardButton(text='Пользоваться ботом', callback_data='check_subscription')]
        ]
    )
    return keyboard


async def start_button_keyboard() -> InlineKeyboardMarkup:
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='Поехали', callback_data='give_access_key')]
        ]
    )
    return keyboard


# async def download_button_keyboard() -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text='💾 Скачать Outline', url='https://go.okno.network/get/outline')],
#             [InlineKeyboardButton(text='Выбрать из списка версий', callback_data='choose_version')]
#         ]
#     )
#     return keyboard
# 
# 
# async def access_key_button_keyboard() -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text='🔑 Получить ключ доступа', callback_data='get_access_key')]
#         ]
#     )
#     return keyboard
# 
# 
# async def upgrade_limit_keyboard() -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text='⭐️ Подключить GOLD-подписку', callback_data='connect_subscription')],
#             [InlineKeyboardButton(text='🎁 Получить +5 ГБ в подарок', callback_data='get_gift')]
#         ]
#     )
#     return keyboard
# 
# 
# async def channel_keyboard() -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text='Перейти в канал', url=config.CHANNEL_LINK)],
#             [InlineKeyboardButton(text='◀️ Назад', callback_data='limit_handler')]
#         ]
#     )
#     return keyboard


# async def payment_keyboard(url: str) -> InlineKeyboardMarkup:
#     keyboard = InlineKeyboardMarkup(
#         inline_keyboard=[
#             [InlineKeyboardButton(text='Перейти к оплате', url=url)],
#             [InlineKeyboardButton(text='Проверить оплату', callback_data='check_payment')]
#         ]
#     )
#     return keyboard
