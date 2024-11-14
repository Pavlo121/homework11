import asyncio
import random

# Функція для "завантаження" сторінки
async def download_page(url: str):
    # Випадковий час завантаження від 1 до 5 секунд
    load_time = random.randint(1, 5)
    await asyncio.sleep(load_time)  # Симуляція завантаження сторінки
    print(f"Сторінка {url} завантажена за {load_time} секунд")

# Функція для одночасного завантаження списку URL
async def main(urls: list):
    # Створення списку завдань для кожного URL
    tasks = [download_page(url) for url in urls]
    # Виконання всіх завдань одночасно
    await asyncio.gather(*tasks)

urls = [
    "https://www.youtube.com",
    "https://www.google.com.ua/?hl=ru",
    "https://lms.ithillel.ua"
]


asyncio.run(main(urls))
