import hashlib
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

def shorten_id(card_id: str) -> str:
    return hashlib.md5(card_id.encode()).hexdigest()[:16]

def get_card_keyboard(card_id, buy_url: str) -> InlineKeyboardMarkup:
    # Если card_id — это словарь, извлечь нужный идентификатор
    if isinstance(card_id, dict):
        card_id = card_id.get("id", "default_value")  # Измените ключ в соответствии с вашей структурой данных

    # Убедитесь, что card_id — строка
    card_id = str(card_id)

    short_card_id = shorten_id(card_id)
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Buy", url=buy_url))
    builder.add(InlineKeyboardButton(text="Add to wishlist", callback_data=f"wish:{short_card_id}"))
    builder.add(InlineKeyboardButton(text="Add to a deck", callback_data=f"deck:{short_card_id}"))
    return builder.as_markup()




