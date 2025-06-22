"""Модуль содержит основные настройки логирования."""
import logging
import sys

from colorlog import ColoredFormatter

from schemas.base import config


def setup_logging(level: str):
    """
    Настройка простого консольного логирования.

    :param level: Глобальный уровень логирования
    """
    # Расширенный формат с временем и местом вызова
    log_format = (
        "%(log_color)s%(asctime)s %(levelname)-8s%(reset)s "  # Время и уровень
        "%(blue)s%(filename)s:%(lineno)d%(reset)s "  # Файл и строка
        "%(log_color)s%(message)s%(reset)s"  # Сообщение
    )

    # Настройка цветов
    formatter = ColoredFormatter(
        log_format,
        datefmt="%Y-%m-%d %H:%M:%S",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "red,bg_white",
        },
        reset=True,
        style="%",
    )

    # Очистка старых обработчиков
    _logger = logging.getLogger()
    _logger.handlers.clear()

    # Настройка вывода в консоль
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    _logger.addHandler(handler)
    _logger.setLevel(level.upper())

setup_logging(config.LOG_LEVEL)
logger = logging.getLogger(__name__)