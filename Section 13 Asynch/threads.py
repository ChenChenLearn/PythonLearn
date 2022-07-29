from threading import Thread
import time


def ask_user():
    start = time.time()
    user_input = input('Enter your name: ')
    greet = f'Hello, {user_input}'
    print(greet)
    print(f'ask_user, {time.time() - start}')


def complex_calculation():
    start = time.time()
    print('Started calculating...')
    [x**2 for x in range(20000000)]
    print(f'complex_calculation, {time.time() - start}')  # for 6s to print


# start = time.time()
# ask_user()
# complex_calculation()
# print(f'Single thread total time: {time.time() - start}')


thread1 = Thread(target=complex_calculation)  # define a thread
thread2 = Thread(target=ask_user)

start = time.time()
thread1.start()  # run a thread
thread2.start()

# tell main thread to wait the above two thread are finish
thread1.join()  # wait thread 1 to finish
thread2.join()  # wait thread 2 to finish
print(f'Two thread total time: {time.time() - start}')
