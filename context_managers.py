# context managers are good for resource management

from contextlib import contextmanager

from threading import Lock

with open("notes.txt", "w") as file:
    file.write("some todo....")
# or the old way
file = open("notes.txt", "w")
try:
    file.write("some todo....")
finally:
    file.close()

# Working with locks
lock = Lock()
with lock:
    pass

# or the old way
lock.acquire()
# process here
lock.release()


# Custom context manager
class ManagedFile:
    def __init__(self, file_name):
        print("init")
        self.file_name = file_name

    def __enter__(self):
        print("enter")
        self.file = open(self.file_name, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        if exc_type is not None:
            print("Exception has been handled")
        print("exit")
        return True


with ManagedFile("notes.txt") as file:
    print("before writing")
    file.write("some text here in managed file.")
    print("after writing")
    file.somemethod()

print("continuing...")


# Custom context manager
@contextmanager
def open_managed_file(file_name):
    f = open(file_name, "w")
    try:
        yield f
    finally:
        f.close()


with open_managed_file("notes.txt") as f:
    f.write("write something")
