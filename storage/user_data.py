import aiofiles
import json
import os

STORAGE_PATH = "storage/user_data.json"

async def init_storage():
    if not os.path.exists(STORAGE_PATH):
        async with aiofiles.open(STORAGE_PATH, "w") as f:
            await f.write(json.dumps({}))

async def save_quote(user_id: int, quote: str):
    await init_storage()
    async with aiofiles.open(STORAGE_PATH, "r+") as f:
        data = json.loads(await f.read() or "{}")
        if str(user_id) not in data:
            data[str(user_id)] = []
        data[str(user_id)].append(quote)
        await f.seek(0)
        await f.write(json.dumps(data, indent=2))

async def get_quotes(user_id: int):
    await init_storage()
    async with aiofiles.open(STORAGE_PATH, "r") as f:
        data = json.loads(await f.read() or "{}")
        return data.get(str(user_id), [])

async def delete_quote(user_id: int, quote_index: int):
    await init_storage()
    async with aiofiles.open(STORAGE_PATH, "r+") as f:
        data = json.loads(await f.read() or "{}")
        if str(user_id) in data and 0 <= quote_index < len(data[str(user_id)]):
            data[str(user_id)].pop(quote_index)
            await f.seek(0)
            await f.write(json.dumps(data, indent=2))
            return True
        return False
