import time


def decorator(func):
    def wrapper_func():
        print('Program execution time: ')
        func()
    return wrapper_func


@decorator
def timer():
    start_time = time.time()
    print(time.time() - start_time)


timer()
