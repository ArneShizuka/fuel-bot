"""/start command"""
from telegram import Update
from telegram.ext import CallbackContext


def start_cmd(update: Update, context: CallbackContext) -> None:
    """Handels the /start command
    Sends a welcome message

    Args:
        update: update event
        context: context passed by the handler
    """
    context.bot.send_message(update.message.chat_id, text="Welcome!")
