import asyncio

async def slow_task():

    print("Завдання розпочато")
    await asyncio.sleep(10)
    print("Завдання завершено")

async def maim():
    try:
        await asyncio.wait_for(slow_task(), timeout=5)
    except asyncio.TimeoutError:
        print("Час очікування перевищено! Завдання не встигло завантажитись")

asyncio.run(maim())