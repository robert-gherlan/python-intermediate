import json
from json import JSONEncoder

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# Serialize
personJSON = json.dumps(person, indent=4, sort_keys=True)

print(person)
print(personJSON)

# Write to file
with open("person.json", "w") as file:
    json.dump(person, file, indent=4)

# Deserialize
person = json.loads(personJSON)
print(person)

# Load from file
with open("example.json", "r") as file:
    person = json.load(file)
    print(person)


# Custom class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Encode custom object
user = User("Max", 27)


def encode_user(o):
    if isinstance(o, User):
        return {"name": o.name, "age": o.age, o.__class__.__name__: True}
    else:
        raise TypeError("Object of type User is not JSON serializable")


userJSON = json.dumps(user, default=encode_user)
print(userJSON)


# Encode with JSON encoder
class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return {"name": o.name, "age": o.age, o.__class__.__name__: True}
        else:
            return JSONEncoder.default(self, o)


userJSON = json.dumps(user, cls=UserEncoder)
print(userJSON)

userJSON = UserEncoder().encode(user)
print(userJSON)


def decode_user(dct):
    if User.__name__ in dct:
        return User(name=dct['name'], age=dct['age'])
    else:
        return dct


user = json.loads(userJSON)
print(user)

user = json.loads(userJSON, object_hook=decode_user)
print(type(user))
