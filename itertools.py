# itertools: product, permutations, combinations, accumulate, groupby and infinite iterators.
import operator

from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby, count, \
    cycle, repeat

a = [1, 2]
b = [3, 4]
result = product(a, b)
print(list(result))

result = product(a, b, repeat=2)
print(list(result))

result = product(b, a)
print(list(result))

# Permutations
a = [1, 2, 3]
perm = permutations(a, 2)

print(list(perm))

# Combinations
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))

comb_wr = combinations_with_replacement(a, 2)
print(list(comb_wr))

# Accumulate
a = [1, 2, 3, 4]
acc = accumulate(a)
print(a)
print(list(acc))

acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

a = [1, 2, 5, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))


# GroupBy
def smaller_than_3(x):
    return x < 3


a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))

group_obj = groupby(a, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

persons = [
    {'name': 'Tim', 'age': 25},
    {'name': 'Dan', 'age': 25},
    {'name': 'Lisa', 'age': 27},
    {'name': 'Claire', 'age': 28}
]
group_obj = groupby(persons, key=lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))

# Count
for i in count(10):
    print(i)
    if i == 15:
        break

# Repeat
for i in repeat(1, 100):
    print(i)

# Cycle
a = [1, 2, 3]
for i in cycle(a):
    print(i)
