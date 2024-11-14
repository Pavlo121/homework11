import aiohttp
import asyncio
import time

async def send_request(session, url):
    async with session.get(url) as response:
        return await response.text()

async def async_requests(url, n):
    async with aiohttp.ClientSession() as session:
        tasks = [send_request(session, url) for _ in range(n)]
        start_time = time.time()
        await asyncio.gather(*tasks)
        end_time = time.time()
        print(f"Асинхронний час: {end_time - start_time:.2f} секунд")

asyncio.run(async_requests("https://www.google.com.ua/?hl=ru", 500))
