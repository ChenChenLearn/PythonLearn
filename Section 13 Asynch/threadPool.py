import time
from concurrent.futures import ThreadPoolExecutor


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print('ask_user: ', time.time() - start)


def complex_calculation():
    print('Started calculating...')
    start = time.time()
    [x**2 for x in range(20000000)]
    print('complex_calculation: ', time.time() - start)


start = time.time()


# create a thread pool
with ThreadPoolExecutor(max_workers=2) as pool:  # create two threads
    pool.submit(complex_calculation)  # start the thread
    pool.submit(ask_user)  # start the thread

pool.shutdown()  # will wait the thread finish

print('Two thread total time: ', time.time() - start)
