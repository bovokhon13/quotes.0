import aiohttp
import asyncio
from config.settings import API_URL
from cachetools import TTLCache
import logging

cache = TTLCache(maxsize=100, ttl=300)  # Кэш на 5 минут

async def fetch_quote():
    try:
        if "quote" in cache:
            return cache["quote"]
        
        async with aiohttp.ClientSession() as session:
            async with session.get(API_URL, timeout=5) as response:
                if response.status == 200:
                    data = await response.json()
                    quote = f"{data.get('content', 'No quote available')} — {data.get('author', 'Unknown')}"
                    cache["quote"] = quote
                    return quote
                else:
                    logging.error(f"API error: {response.status}")
                    return "Error fetching quote"
    except asyncio.TimeoutError:
        logging.error("API request timed out")
        return "Request timed out"
    except Exception as e:
        logging.error(f"API request failed: {e}")
        return "Failed to fetch quote"
