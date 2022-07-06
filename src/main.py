import os

import dotenv
from telegram.ext import Updater

from modules.handlers import add_handlers


def main() -> None:
    dotenv.load_dotenv()
    updater = Updater(
        os.getenv("TOKEN"),
        request_kwargs={"read_timeout": 20, "connect_timeout": 20},
        use_context=True,
    )

    add_handlers(updater.dispatcher)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
