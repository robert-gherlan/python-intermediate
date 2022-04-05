mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, True, "apple", "apple"]
print(mylist2)

first_item = mylist[0]  # first item
last_item = mylist[-1]  # last item
print(first_item)
print(last_item)

for item in mylist:
    print(item)

if "banana" in mylist:
    print("banana is in the list")

print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1, "blueberry")
print(mylist)

item = mylist.pop()
print(item)
print(mylist)

item1 = mylist.remove("cherry")
print(item1)
print(mylist)

mylist.reverse()
print(mylist)

mylist.sort()
print(mylist)

new_list = sorted(mylist)
print(new_list)

mylist.clear()
print(mylist)

mylist3 = [0] * 5
print(mylist3)

mylist4 = [1, 2, 3, 4, 5]
new_list = mylist3 + mylist4
print(new_list)

mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
a = mylist[1:5]  # slice from index 1 to 5(5 is excluded)
print(a)
a = mylist[:3]  # slice from index 0 to 3(3 is excluded)
print(a)
a = mylist[3:]  # slice from index 3 to end(3 is excluded)
print(a)
a = mylist[::2]  # get values from 2 in 2 as index
print(a)

list_org = ["banana", "cherry", "apple"]
list_copy = list_org.copy()
list_copy = list_org[:]
print(list_copy)

mylist = [1, 2, 3, 4, 5, 6]
b = [i * i for i in mylist]
print(b)
