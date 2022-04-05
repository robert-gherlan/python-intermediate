import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper():
        print("start")
        func()
        print("end")

    return wrapper


@start_end_decorator
def print_name():
    print("Alex")


print_name()


# Decorators with arguments
def start_end_decorator_arguments(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        func_result = func(*args, **kwargs)
        print("end")
        return func_result

    return wrapper


@start_end_decorator_arguments
def add5(x):
    return x + 5


result = add5(10)
print(result)

print(help(add5))
print(add5.__name__)


# Decorators with arguments
def repeat(num_times: int):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                func_result = func(*args, **kwargs)
            return func_result

        return wrapper

    return decorator_repeat


@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")


greet("Alex")


# Nested decorators
def start_end_decorator_nested(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("start")
        func_result = func(*args, **kwargs)
        print("end")
        return func_result

    return wrapper


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result

    return wrapper


@debug
@start_end_decorator_nested
def say_hello(name):
    greeting = f"Hello {name}"
    print(greeting)
    return greeting


say_hello("Alex")


# Class decorators
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)


@CountCalls
def say_hello():
    print("Hello")


say_hello()
say_hello()
