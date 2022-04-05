import random
import secrets
import numpy as np

a = random.random()
print(a)

a = random.uniform(1, 10)
print(a)

a = random.randint(1, 10)
print(a)

a = random.randrange(1, 10)
print(a)

a = random.normalvariate(0, 1)
print(a)

my_list = list("ABCDEF")
print(my_list)

a = random.choice(my_list)
print(a)

a = random.sample(my_list, 3)
print(a)

a = random.choices(my_list, k=3)
print(a)

random.shuffle(my_list)
print(my_list)

# Seed
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

# Secrets
a = secrets.randbelow(10)
print(a)

a = secrets.randbits(4)
print(a)

my_list = list("ABCDEFGH")
a = secrets.choice(my_list)
print(a)

# NumPy
a = np.random.rand(3)
print(a)

a = np.random.rand(3, 3)
print(a)

a = np.random.randint(0, 10, 3)
print(a)

a = np.random.randint(0, 10, (3, 4))
print(a)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
np.random.shuffle(arr)
print(arr)

np.random.seed(1)
print(np.random.rand(3, 3))
np.random.seed(2)
print(np.random.rand(3, 3))
