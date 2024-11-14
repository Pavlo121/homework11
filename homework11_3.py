import asyncio
import queue


async def producer(queue):
# Додає 5 завдань до черги із затримкою 1 секунда між додаваннями.
    for i in range(1, 6):
        await asyncio.sleep(1)
        task = f"Task {i}"
        await queue.put(task)
        print(f"Producer додав {task} до черги")

async def consumer(queue, consumer_id):
# Забирає завдання з черги та обробляє його із затримкою 2 секунди.
    while True:
        task = await queue.get()
        print(f"Consumer {consumer_id} отримав {task}")
        await asyncio.sleep(1)
        print(f"Consumer {consumer_id} завершив {task}")
        queue.task_done()

async def main():
    queue = asyncio.Queue()

    producer_task = asyncio.create_task(producer(queue))

    consumer_tasks = [asyncio.create_task(consumer(queue, i)) for i in range(2)]

    await producer_task

    await queue.join()

    for c in consumer_tasks:
        c.cancel()

    await asyncio.gather(*consumer_tasks, return_exceptions=True)

asyncio.run(main())