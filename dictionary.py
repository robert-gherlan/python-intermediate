mydict = {"name": "Max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Mary", age=27, city="Boston")
print(mydict2)

value = mydict['name']
print(value)

value = mydict['age']
print(value)

# value = mydict['no_existing'] throw error
# print(value)

# Add items
mydict["email"] = "max@xyz.com"
print(mydict)
mydict["email"] = "coolmax@xyz.com"
print(mydict)

# Delete items
del mydict["email"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()  # remove the latest inserted item
print(mydict)

if "name" in mydict:
    print(mydict["name"])

# Iterate
for key in mydict2.keys():
    print(key)

for value in mydict2.values():
    print(value)

for key, value in mydict2.items():
    print(key, value)

# Copy a dictionary
mydict_copy = mydict2.copy()
print(mydict_copy)
mydict_copy = dict(mydict2)
print(mydict_copy)

# Merge dictionary
my_dict = {"name": "Max", "age": 28, "email": "max@xyz.com"}
my_dict_2 = dict(name="Mary", age=27, city="Boston")
my_dict.update(my_dict_2)
print(my_dict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3]
print(value)

my_tuple = (8, 7)
mydict = {my_tuple: 15}
print(mydict)
