import aiohttp
import asyncio


async def download_image(url, filename):
# Завантажує зображення з вказаного URL та зберігає його у файл.
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                with open(filename, 'wb') as f:
                    f.write(await response.read())
                print(f"Зображення збережено як {filename}")
            else:
                print(f"Не вдалося завантажити {url}, статус: {response.status}")


async def main():
    image_urls = [
        ("https://cdn.pixabay.com/photo/2024/10/27/07/12/women-9152739_1280.jpg", "image1.jpg"),
        ("https://cdn.pixabay.com/photo/2024/11/03/22/57/dogs-9172481_1280.jpg", "image2.jpg"),
        ("https://cdn.pixabay.com/photo/2024/05/19/13/40/daisy-8772631_1280.jpg", "image3.jpg"),
    ]

    tasks = [download_image(url, filename) for url, filename in image_urls]

    await asyncio.gather(*tasks)


asyncio.run(main())
