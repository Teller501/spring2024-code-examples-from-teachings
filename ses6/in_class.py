from datetime import datetime
import time

# First class functions


def f1(p):
    return p


def foo():
    return 'Hello from foo'


# Inner functions
def foo():

    # define
    def bar():
        return 'From bar'

    # execute
    return bar()

# Decorators


def add_text(func):
    def wrapper(*args):
        print('Summen af de to tal: ')
        func(*args)
    return wrapper


@add_text
def add(n1, n2):
    print(n1 + n2)


# wrapper = add_text(add)


# Exercise 1 - Decorating add


def log_add(func):
    def wrapper(*args):
        with open('log.txt', 'a') as file:
            file.write(
                f'{datetime.now()}: Add called with args: {args} result is {func(*args)}\n')

    return wrapper


@log_add
def add(*args):
    return sum(args)


@log_add
def printer(text):
    return text


# Exercise 2 - Time it
def time_it(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f'{func.__name__} took {end - start} seconds')
        return result
    return wrapper


@time_it
def add(*args):
    return sum(args)


# Exercise 3 - Decorator skills evaluation
def simple_logger(func):
    def wrapper():
        print(f'Function {func.__name__}')
        return func()

    return wrapper


@simple_logger
def test_func():
    return 'Inside test_func'


def repeat(num_times):
    def decorator(func):
        def wrapper():
            for _ in range(num_times):
                func()
        return wrapper
    return decorator


@repeat(3)
def print_hello():
    print('Hello')


def modify_args(func):
    def wrapper(*args):
        args = [arg * 2 for arg in args]
        return func(*args)
    return wrapper


@modify_args
def add_numbers(*args):
    return sum(args)
# Exercise 4 - Decorating Game Characters


def sharpshooter(func):
    def wrapper():
        return f'{func()}, the sharpshooter'
    return wrapper


@sharpshooter
def player():
    return "I'm the player character"


print(player())


# Exercise 5 - Menu register
menu = dict()


def register(func):
    menu[func.__name__] = func
    return func

@register
def home():
     return 'I´m the home page'