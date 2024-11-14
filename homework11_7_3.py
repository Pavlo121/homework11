import requests
import time
from concurrent.futures import ProcessPoolExecutor

def send_request(url):
    response = requests.get(url)
    return response

def process_requests(url, n):
    start_time = time.time()
    with ProcessPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(send_request, url) for _ in range(n)]
        for future in futures:
            future.result()
    end_time = time.time()
    print(f"Багатопроцесорний час: {end_time - start_time:.2f} секунд")

# Запуск
process_requests("https://www.google.com.ua/?hl=ru", 500)
