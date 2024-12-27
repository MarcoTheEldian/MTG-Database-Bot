from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from services.card_search.service import card_search
from bot.keyboards.inline import get_card_keyboard

router = Router()

@router.message(Command("find"))
async def cmd_find(message: Message, command: CommandObject):
    query = command.args
    if not query:
        await message.reply("Пожалуйста, введите название карты для поиска.")
        return

    cards = await card_search(query)
    if not cards:
        await message.reply("Карты не найдены. Попробуйте уточнить запрос.")
        return

    card = cards[0]
    name = card.get("name")
    image_url = card.get("image_uris", {}).get("normal", "")
    price = card.get("prices", {}).get("usd", "Цена недоступна")
    buy_url = card.get("purchase_uris", {}).get("tcgplayer", "")

    keyboard = get_card_keyboard(card, buy_url)

    await message.reply_photo(
        photo=image_url,
        caption=f"**{name}**\nЦена: {price}$",
        reply_markup=keyboard,
        parse_mode="Markdown"
    )