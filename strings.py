my_string = "Hello World"
print(my_string)

my_string = 'I\'m a programmer'
print(my_string)

my_string = """
    Multiline strings \
    Documentation purpose
"""
print(my_string)

my_string = "Hello World"
char = my_string[0]
print(char)

substring = my_string[1:5]
print(substring)

reversed_string = my_string[::-1]
print(reversed_string)

greeting = "Hello"
name = "Tom"
sentence = greeting + " " + name
print(sentence)

for char in greeting:
    print(char)

if "Hel" in greeting:
    print("exists")

my_string = "     Hello World    "
print(my_string)
print(my_string.strip())

my_string = "Hello World"
print(my_string.upper())
print(my_string.lower())
print(my_string.startswith("H"))
print(my_string.endswith("World"))
print(my_string.find("o"))
print(my_string.find("lo"))
print(my_string.find("ppp"))
print(my_string.count("o"))
print(my_string.count("p"))
print(my_string.replace("World", "Universe"))

my_string = "how are you doing"
my_list = my_string.split(" ")
print(my_list)

my_string = "how,are,you,doing"
my_list = my_string.split(",")
print(my_list)

new_string = " ".join(my_list)
print(new_string)

my_list = ["a"] * 6
print(my_list)
my_string = "".join(my_list)
print(my_string)

# Format strings
var = "Tom"
my_string = "the variable is %s" % var
print(my_string)

my_string = "the variable is {}".format(var)
print(my_string)

my_string = f"the variable is {var}"
print(my_string)