import requests
import time
from concurrent.futures import ThreadPoolExecutor

def send_request(url):
    response = requests.get(url)
    return response

def thread_requests(url, n):
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_request, url) for _ in range(n)]
        for future in futures:
            future.result()
    end_time = time.time()
    print(f"Багатопотоковий час: {end_time - start_time:.2f} секунд")

# Запуск
thread_requests("https://www.google.com.ua/?hl=ru", 500)
