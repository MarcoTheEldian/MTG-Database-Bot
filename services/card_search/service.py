import aiohttp
from core.config import Config  # Ваш конфиг

API_URL = Config.SKRYFALL_BASE_URL + "/cards/search"

async def card_search(query: str):
    async with aiohttp.ClientSession() as session:
        params = {"q": query}
        try:
            async with session.get(API_URL, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get("data", [])
                elif response.status == 404:
                    return []
                else:
                    print(f"API Error: {response.status}")
                    return []
        except aiohttp.ClientError as e:
            print(f"Connection Error: {e}")
            return []