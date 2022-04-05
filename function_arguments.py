def print_name(name):  # the "name" is the parameter name
    print(name)


print_name("Alex")  # the "Alex" is the argument


def foo(a, b, c, d=4):  # the "d" parameter is a default parameter and must be at the end of the function
    print(a, b, c, d)


foo(1, 2, 3)  # These are positional arguments
foo(a=1, b=2, c=3)  # These are keyword arguments
foo(c=1, b=2, a=3)
foo(1, b=2, c=3)  # Combination of positional and keywords arguments

foo(1, 2, 3, 4)


def function(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])


function(1, 2)
function(1, 2, 3, 4, 5)
function(1, 2, six=6, seven=7)
function(1, 2, 3, 4, 5, six=6, seven=7)


def function1(a, b, *, c, d):  # every argument after * must be a keyword argument
    print(a, b, c, d)


function1(1, 2, c=3, d=4)


def function2(*args, last):
    for arg in args:
        print(arg)
    print(last)


function2(1, 2, 3, last=4)


# Unpacking arguments
def foo(a, b, c):
    print(a, b, c)


my_list = [0, 1, 2]  # must match the number of parameters
my_tuple = (0, 1, 2)  # must match the number of parameters
foo(*my_list)  # Unpacking arguments
foo(*my_tuple)  # Unpacking arguments

my_dict = {"a": 1, "b": 2, "c": 3}
foo(**my_dict)  # Unpacking arguments from dictionary


# Local and global variables
def foo():
    global number
    x = number
    number = 3
    print("number inside function", x)


number = 0

foo()

print(number)


# Parameter passing
# call by object, or call by object reference
# parameters passed in are reference to a object
# reference are passed as value

def foo(x):
    x = 5


var = 10
foo(var)
print(var)


def foo(a_list):
    a_list += [200, 300, 400]
    a_list.append(4)
    a_list[0] = -100


my_list = [1, 2, 3]
foo(my_list)
print(my_list)
