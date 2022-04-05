import copy

org = 5
cpy = org
print(cpy)

org = [1, 2, 3, 4, 5]
cpy = copy.copy(org)
print(cpy)
cpy = org.copy()
print(cpy)
cpy = list(org)
print(cpy)
cpy = org[:]
print(cpy)

org = [[1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.copy(org)
cpy[0][1] = -10
print(cpy)
print(org)

org = [[1, 2, 3, 4], [5, 6, 7, 8, 9]]
cpy = copy.deepcopy(org)
cpy[0][1] = -10
print(cpy)
print(org)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Company:
    def __init__(self, boss, employee):
        self.boss = boss
        self.employee = employee


p1 = Person("Alex", 27)
p2 = copy.copy(p1)
p2.age = 28
print(p2.age)
print(p1.age)

boss = Person("Alex", 55)
employee = Person("Joe", 27)
company = Company(boss, employee)
company_clone = copy.deepcopy(company)
company_clone.boss.age = 56
print(company_clone.boss.age)
print(company.boss.age)
