from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

router = Router()

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("""
    Command list:
    /help - Show commands list
    /find - display a card by name
    /decks - show your decks
    /wish - show your wishlist 
    """)