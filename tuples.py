my_tuple = ("Max", 28, "Boston")
print(my_tuple)

my_tuple = ("Max",)
print(type(my_tuple))

my_tuple = tuple(["max", 28, "Boston"])
print(my_tuple)

item = my_tuple[1]
print(item)

item = my_tuple[-1]
print(item)

for item in my_tuple:
    print(item)

if 28 in my_tuple:
    print("28 is in my tuple")

print(len(my_tuple))

my_tuple = ('a', 'p', 'p', 'l', 'e')
print(my_tuple.count('p'))
print(my_tuple.count('o'))

print(my_tuple.index('p'))
print(my_tuple.index('a'))
print(my_tuple.index('l'))

my_list = list(my_tuple)
print(type(my_list))

my_tuple2 = tuple(my_list)
print(type(my_tuple2))

# Slicing
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)
b = a[:5]
print(b)
b = a[2:]
print(b)
b = a[::-1]  # To reverse tuple
print(b)

# Unpacking
my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4)
i1, *i2, i3 = my_tuple
print(i1)
print(i2)
print(i3)
