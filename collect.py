# collections: Counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter, namedtuple, defaultdict, deque, OrderedDict

# Counter
a = "aaaaabbbbccccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1)[0][0])
print(list(my_counter.elements()))

# namedtuple
Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)
print(pt.x)
print(pt.y)

# OrderedDict
ordered_dict = OrderedDict()
ordered_dict["b"] = 2
ordered_dict["b"] = 3
ordered_dict["d"] = 4
ordered_dict["a"] = 1
print(ordered_dict)

# defaultdict
default_dict = defaultdict(list)
default_dict["a"] = 1
default_dict["b"] = 2
print(default_dict)
print(default_dict['c'])

# deque
deque = deque()
deque.append(1)
deque.append(2)
deque.appendleft(3)
print(deque)
deque.pop()
print(deque)
deque.popleft()
print(deque)
deque.extend([4, 5, 6])
print(deque)
deque.extendleft([6, 7, 8])
print(deque)
deque.rotate(1)
print(deque)