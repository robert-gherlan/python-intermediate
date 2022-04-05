# Working with threads and queues
from threading import Thread, Lock, current_thread
from queue import Queue


def work_with_queues():
    q = Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    first = q.get()
    print(first)
    is_empty = q.empty()
    print(is_empty)
    # q.task_done()  # this need to be called when the job is done
    # q.join()  # blocks until al items are processed.


def worker(queue: Queue, lock: Lock):
    while True:
        value = queue.get()
        with lock:
            # processing
            print(f"in {current_thread().name} got {value}")
            queue.task_done()


if __name__ == "__main__":
    queue = Queue()
    lock = Lock()
    num_threads = 10
    for i in range(num_threads):
        thread = Thread(target=worker, args=(queue, lock))
        thread.daemon = True
        thread.start()

    for i in range(1, 21):
        queue.put(i)

    queue.join()

    print("END MAIN")

    work_with_queues()
