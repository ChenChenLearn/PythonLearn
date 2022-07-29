from itertools import count


def countdown(n):
    while n > 0:
        yield n
        n -= 1


# c1 = countdown(10)
# c2 = countdown(20)
# print(next(c1))  # 10
# print(next(c2))  # 20
# print(next(c1))  # 9
# print(next(c2))  # 19

# without using threads
tasks = [countdown(10), countdown(5), countdown(20)]
while tasks:
    task = tasks[0]
    tasks.remove(task)
    try:
        x = next(task)
        print(x)
        task.append(task)
    except StopIteration:
        print('Task finished')
