myset = {1, 2, 3, 1, 2}
print(myset)

myset = set([1, 2, 3, 4, 1, 3, 4])
print(myset)

my_set = set("Hello")
print(my_set)

# Empty set
empty_set = {}
print(type(empty_set))

empty_set = set()
print(type(empty_set))

empty_set.add(1)
empty_set.add(2)
empty_set.add(3)
print(empty_set)

# Remove from set
empty_set.remove(3)
print(empty_set)

empty_set.discard(2)
print(empty_set)

empty_set.clear()

item = myset.pop()
print(item)

# Iterate
for item in myset:
    print(item)

if 1 in myset:
    print("1 is in myset")

# Calculations
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union = odds.union(evens)
print(union)

intersection = odds.intersection(evens)
print(intersection)

intersection = odds.intersection(primes)
print(intersection)

intersection = evens.intersection(primes)
print(intersection)

setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}
difference = setA.difference(setB)
print(difference)

difference = setB.difference(setA)
print(difference)

difference = setA.symmetric_difference(setB)
print(difference)

difference = setB.symmetric_difference(setA)
print(difference)

setA.copy().update(setB.copy())
print(setA)

setA.copy().difference_update(setB.copy())
print(setA)

setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}
setC = {7, 8}
print(setA.issubset(setB))
print(setB.issubset(setA))
print(setA.issuperset(setB))

print(setA.isdisjoint(setB))
print(setA.isdisjoint(setC))

setD = setA.copy()
print(setD)

a = frozenset([1, 2, 3, 4])
print(a)
print(type(a))
