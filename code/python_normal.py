import datetime

import math


def main():

    start = datetime.datetime.now()

    compute(end=50000000)

    time = datetime.datetime.now() - start

    print(f"Finish in {time.total_seconds():.2f} s")


def compute(end, start=1):
    pos = start

    factor = 1000 * 1000

    while pos < end:
        pos += 1
        math.sqrt((pos - factor) * (pos - factor))


if __name__ == "__main__":
    main()

"""
Finish in 12.67 s
"""