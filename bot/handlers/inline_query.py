from aiogram import Router
from aiogram.types import InlineQuery, InlineQueryResultPhoto
from services.card_search.service import card_search

router = Router()


@router.inline_query()
async def inline_card_search(inline_query: InlineQuery):
    query = inline_query.query
    if not query:
        return

    cards = await card_search(query)
    results = []

    for card in cards[:10]:
        if "image_uris" not in card:
            continue

        results.append(
            InlineQueryResultPhoto(
                id=card["id"],
                photo_url=card["image_uris"]["normal"],
                thumbnail_url=card["image_uris"]["normal"],  # Use thumbnail_url instead of thumb_url
                title=card["name"],
                description=card.get("oracle_text", "No oracle"),
                caption=f"**{card['name']}**\nPrice: ${card.get('prices', {}).get('usd', 'N/A')}",
            )
        )

    if results:
        await inline_query.answer(results, cache_time=1)
    else:
        await inline_query.answer([], switch_pm_text="Карта не знайдена", switch_pm_parameter="start")
