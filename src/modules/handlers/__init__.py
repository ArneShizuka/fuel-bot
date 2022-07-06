"""Moduels that hanlde the events that bot recognizes and reacts to"""
from telegram.ext import CommandHandler, Dispatcher

from .start import start_cmd


def add_handlers(disp: Dispatcher) -> None:
    """Adds all the needed handlers to the dispatcher

    Args:
        disp: suppyed dispatcher
    """

    # Command handlers
    disp.add_handler("start", start_cmd)
