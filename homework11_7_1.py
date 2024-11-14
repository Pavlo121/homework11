import requests
import time

def send_request(url):
    response = requests.get(url)
    return response

def sync_requests(url, n):
    start_time = time.time()
    for _ in range(n):
        send_request(url)
    end_time = time.time()
    print(f"Синхронний час: {end_time - start_time:.2f} секунд")

# Запуск
sync_requests("https://www.google.com.ua/?hl=ru", 500)