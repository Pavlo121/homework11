from sqlite3 import connect

import aiohttp
import asyncio

async def fetch_content(url: str):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    content = await response.text()
                    print(f"Сторінка {url} завантажена успішно")
                    return content
                else:
                    print(f"Помилка {response.status} при завантаженні {url}")
                    return f"Помилка {response.status}"
    except aiohttp.ClientError as e:
        print(f"Помилка підключення до {url}: {e}")
        return f"Помилка підключення: {e}"

async def fetch_all(urls: list):
    tasks = [fetch_content(url) for url in urls]
    contents = await asyncio.gather(*tasks)

    for url, content in zip(urls, contents):
        print(f"\nВміст для {url}:\n{content[:100]}...")

urls = [
    "https://www.youtube.com",
    "https://www.google.com.ua/?hl=ru",
    "https://lms.ithillel.ua"
]

asyncio.run(fetch_all(urls))


