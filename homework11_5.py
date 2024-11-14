from aiohttp import web
import asyncio

async def handle_root(request):
# Маршрут /, який повертає 'Hello, World!
    return web.Response(text="Hello, world")

async def handle_slow(request):
# Маршрут /slow, який симулює довгу операцію із затримкою в 5 секунд
    await asyncio.sleep(5)
    return web.Response(text="Operation completed")

app = web.Application()
app.add_routes([
    web.get("/", handle_root),
    web.get("/slow", handle_slow),
])

if __name__ == "__main__":
    web.run_app(app, host="127.0.0.1", port=8080)