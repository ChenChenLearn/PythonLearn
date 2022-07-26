from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def get_friend():
    yield from friends  # like a for loop


c = get_friend()
print(next(c))
print(next(c))


def greet(g):
    while True:
        try:
            friend = next(g)
            yield f'Hello {friend}'
        except StopIteration:
            pass


friends_generator = get_friend()
g = greet(friends_generator)
print(next(g))
print(next(g))
