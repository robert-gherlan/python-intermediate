from multiprocessing import Process, Value, Array, Lock, Queue
from threading import Thread
import os
import time


# Working with processes
def square_numbers(limit):
    for value in range(limit):
        value * value
        time.sleep(0.1)


def work_with_processes():
    processes = []
    number_of_processes = os.cpu_count()
    # create processes
    for i in range(number_of_processes):
        p = Process(target=square_numbers, args=(10,))
        processes.append(p)
    # start processes
    for p in processes:
        p.start()
    # join processes
    for p in processes:
        p.join()
    print("END PROCESSES")


def work_with_threads():
    # Working with threads
    threads = []
    number_of_threads = 10
    # create threads
    for i in range(number_of_threads):
        t = Thread(target=square_numbers, args=(10,))
        threads.append(t)
    # start threads
    for t in threads:
        t.start()
    # join threads
    for t in threads:
        t.join()
    print("END THREADS")


def add_100(number: Value, lock: Lock):
    for i in range(100):
        time.sleep(0.01)
        with lock:
            number.value += 1


def work_with_processes_shared_value():
    lock = Lock()
    shared_number = Value('i', 0)
    print("Number at beginning is", shared_number.value)

    p1 = Process(target=add_100, args=(shared_number, lock))
    p2 = Process(target=add_100, args=(shared_number, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Number at end is", shared_number.value)
    print("END PROCESSES SHARED VARIABLE")


def add_100_array(numbers: Array, lock: Lock):
    for i in range(100):
        time.sleep(0.01)
        for j in range(len(numbers)):
            with lock:
                numbers[j] += 1


def work_with_processes_shared_array():
    lock = Lock()
    shared_array = Array('d', [0.0, 100.0, 200.0])
    print("Array at beginning is", shared_array[:])

    p1 = Process(target=add_100_array, args=(shared_array, lock))
    p2 = Process(target=add_100_array, args=(shared_array, lock))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Array at end is", shared_array[:])
    print("END PROCESSES SHARED ARRAY")


def square(numbers, queue):
    for i in numbers:
        queue.put(i * i)


def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1 * i)


def work_with_processes_queue():
    numbers = range(1, 6)
    queue = Queue()

    p1 = Process(target=square, args=(numbers, queue))
    p2 = Process(target=make_negative, args=(numbers, queue))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    while not queue.empty():
        print(queue.get())

    print("END PROCESSES QUEUE")


if __name__ == "__main__":
    work_with_processes_queue()

    work_with_processes_shared_array()

    work_with_processes_shared_value()

    work_with_processes()

    work_with_threads()
