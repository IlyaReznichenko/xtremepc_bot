"""Модуль содержит основные настройки логирования."""
# src/core/logging.py
import logging
import sys


def setup_logging(level: str = "INFO") -> logging.Logger:
    """
    Настройка простого консольного логирования

    Уровни: DEBUG, INFO, WARNING, ERROR, CRITICAL
    """
    logger = logging.getLogger()
    logger.setLevel(level.upper())

    # Очистка предыдущих обработчиков
    logger.handlers.clear()

    # Настройка вывода в консоль
    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(level.upper())

    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger

# Инициализация глобального логгера
logger = setup_logging("INFO")