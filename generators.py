import sys


# Advantage of generators // memory consumption // time consumption
def first_n(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums


def first_n_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1


print(first_n(10))
print(sum(first_n(10)))

print(list(first_n_generator(10)))
print(sum(first_n_generator(10)))

print(sys.getsizeof(first_n(1_000_000)))
print(sys.getsizeof(first_n_generator(1_000_000)))


def fibonacci(limit):
    # 0 1 1 2 3 5 8
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


fib = fibonacci(30)
for i in fib:
    print(i)

my_generator = (i for i in range(10) if i % 2 == 0)
print(sys.getsizeof(my_generator))
print(my_generator)
print(list(my_generator))
for i in my_generator:
    print(i)

list_comprehension = [i for i in range(10) if i % 2 == 0]
print(list_comprehension)
print(sys.getsizeof(list_comprehension))


# Countdown
def countdown(num):
    print("starting")
    while num > 0:
        yield num
        num -= 1


cd = countdown(5)

value = next(cd)
print(value)

value = next(cd)
print(value)


# Iterate over generators
def my_generator():
    yield 3
    yield 2
    yield 1


g = my_generator()
print(g)

print(sum(g))

print(sorted(g))

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

value = next(g)
print(value)

for i in g:
    print(i)
