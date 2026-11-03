
import asyncio
import logging

from telethon import TelegramClient
from telethon.sessions import StringSession

from config.config import Config
from utils.thanos import thanos_protect
from startup.startup import start_bot
from core.console import ColourFormatter


logging.basicConfig(
    level=logging.WARNING,
    handlers=[logging.StreamHandler()]
)

logging.getLogger().handlers[0].setFormatter(
    ColourFormatter("cipherelite")()
)

# Initialize Telegram session
eliteses = thanos_protect(Config.1BVtsOIMBu3q7Pb_K3EMZtCdUGgpyJMTAw4pKloP8H-81RKCTshyqt_j50CGfi1sKAliz10dmE-YLQpNSEbCJ-pdq88puUV7G1dRoQlME4VSWk-7JGcsB3hg_Acx8rEvH3AgaQaUoaur3472BsR5L1npnS-plRNCnzryjJKM4CwmanOLgzyWaWnD8C6qKpdLYnNT08GWxf4PAVjXXTr96ZX3kOq3RNTPjmHw9PJ-xkzM3PadF5wEFGsqnlZOeawdS9qJ45mic1TdesmQ2Yd5HkSqh1i5U-wGhU3U078xn8G1ccDgOFjzlvXfhzMGUfn-ybm6lXXO6zI3_jE1muiy5BmfaCjDXA5M_x_gMafUqVhE5RGvac-53fBfM=)

# Initialize Telegram client
client = TelegramClient(
    StringSession(eliteses),
    Config.App.api_id=38877165,
    Config.App.api_hash=7b4223da1f0741a6510901da67e3bed4 
)


async def main():
    await client.connect()

    if not await client.is_user_authorized():
        raise RuntimeError(
            "Telegram session is invalid or unauthorized. "
            "Generate a new session string."
        )

    print("Telegram client connected successfully!")

    await start_bot(client)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped!")

