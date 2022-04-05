result = 5 * 7
print(result)

result = 2 ** 4  # pow operation
print(result)

zeros = [0] * 10  # list with ten zeroes
print(zeros)

list = [0, 1] * 10
print(list)

zeros = (0,) * 10  # tuple with ten zeroes
print(zeros)

tuple = (0, 1) * 10
print(tuple)

string = "AB" * 10  # ten times AB string
print(string)


def function(a, b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key, kwargs[key])


function(1, 2, 3, 4, 5, six=6, seven=7)

# unpack
numbers = [1, 2, 3, 4, 5, 6]
*beginning, last = numbers
print(beginning, last)

beginning, *last = numbers
print(beginning, last)

beginning, *middle, secondlast, last = numbers
print(beginning, middle, secondlast, last)

# merge lists
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

# merge dictionary
dict_a = {"a": 1, "b": 2}
dict_b = {"c": 3, "d": 4}
my_dict = {**dict_a, **dict_b}
print(my_dict)
