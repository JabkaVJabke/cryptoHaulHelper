import time
from threading import Thread
from selenium import webdriver


def create_driver_threaded(thread_id: int, result_container: list):
    options = webdriver.FirefoxOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    result_container[thread_id] = webdriver.Firefox(options=options)


def create_drivers(drivers_count: int):
    start_time = time.time()
    results = [None] * drivers_count
    threads = [None] * drivers_count
    for i in range(drivers_count):
        threads[i] = Thread(target=create_driver_threaded, args=(i, results))
        threads[i].start()

    for i in range(drivers_count):
        threads[i].join()

    print('Drivers count:', drivers_count)
    print('Drivers start time:', time.time() - start_time)
    return results
