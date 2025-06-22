"""Модуль содержит конечный автомат состояний (утилита aiogram)."""

from aiogram.fsm.state import State, StatesGroup


class Start(StatesGroup):
    start_message_id = State()


class UserState(StatesGroup):
    user_id = State()
    username = State()


# class AccessKey(StatesGroup):
#     access_key_message_id = State()
#
#
# class Paying(StatesGroup):
#     payment_message_id = State()


class MessageDelete(StatesGroup):
    message_id = State()