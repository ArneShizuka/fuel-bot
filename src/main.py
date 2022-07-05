import os

import dotenv
from telegram.ext import Updater


def main() -> None:
    dotenv.load_dotenv()
    updater = Updater(
        os.getenv("TOKEN"),
        request_kwargs={"read_timeout": 20, "connect_timeout": 20},
        use_context=True,
    )

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
