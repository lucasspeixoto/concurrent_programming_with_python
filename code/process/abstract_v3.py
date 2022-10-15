#from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor

import time


def process():
    print("[", end="", flush=True)

    for _ in range(1, 11):
        print("#", end="", flush=True)
        time.sleep(1)

    print("]", end="", flush=True)
    
    return 30


def main():
    with Executor() as executor:
        future = executor.submit(process)
        
    print(f'\nReturn: {future.result()}')


if __name__ == "__main__":
    main()
