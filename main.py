import os
import sys
import time
import asyncio
import random

try:
    from telegram import Bot
    from telegram.error import RetryAfter, TelegramError
    from colorama import Fore, init
except ModuleNotFoundError:
    print("Installing modules...")
    os.system("pip install python-telegram-bot==20.7 colorama")
    from telegram import Bot
    from telegram.error import RetryAfter, TelegramError
    from colorama import Fore, init

init(autoreset=True)

def clear():
    os.system("clear")

async def main():
    print("Tool Running...")

asyncio.run(main())
