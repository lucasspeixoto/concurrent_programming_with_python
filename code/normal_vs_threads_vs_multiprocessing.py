from concurrent.futures import ProcessPoolExecutor
import threading
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor

import datetime

import math


def pure_python():

    start = datetime.datetime.now()

    compute(end=50000000)

    time = datetime.datetime.now() - start

    print(f"Pure Finish in {time.total_seconds():.2f} s")


def python_with_threads():

    cores = multiprocessing.cpu_count()

    # print(f"Cores: {cores}")

    start = datetime.datetime.now()

    threads = []
    for n in range(1, cores + 1):
        _start = 50000000 * (n - 1) / cores
        _end = 50000000 * n / cores

        # print(f"Core {n} processado de {_start} até {_end}")

        threads.append(
            threading.Thread(
                target=compute, kwargs={"start": _start, "end": _end}, daemon=True
            )
        )

    [thread.start() for thread in threads]

    [thread.join() for thread in threads]

    time = datetime.datetime.now() - start

    print(f"With Threads Finish in {time.total_seconds():.2f} s")


def python_with_multiprocessing():

    cores = multiprocessing.cpu_count()

    start = datetime.datetime.now()

    with ProcessPoolExecutor(max_workers=cores) as executor:
        for n in range(1, cores + 1):
            _start = 50000000 * (n - 1) / cores
            _end = 50000000 * n / cores

            executor.submit(compute, start=_start, end=_end)

    time = datetime.datetime.now() - start

    print(f"With Multiprocessing Finish in {time.total_seconds():.2f} s")


def main():
    pure_python()

    python_with_threads()

    python_with_multiprocessing()


def compute(end, start=1):
    pos = start

    factor = 1000 * 1000

    while pos < end:
        pos += 1
        math.sqrt((pos - factor) * (pos - factor))


if __name__ == "__main__":
    main()

"""
Pure Finish in 13.92 s
With Threads Finish in 10.68 s
With Multiprocessing Finish in 4.18 s

"""
