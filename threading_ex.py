# Working with threads and locks
from threading import Thread, Lock
import time

database_value = 0


def increase(thread_lock: Lock):
    global database_value

    with thread_lock:
        local_copy = database_value
        # processing
        local_copy += 1
        time.sleep(0.1)

        database_value = local_copy


if __name__ == "__main__":
    print("Start value", database_value)
    lock = Lock()
    thread1 = Thread(target=increase, args=(lock,))
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print("End value", database_value)

    print("END THREADS")
