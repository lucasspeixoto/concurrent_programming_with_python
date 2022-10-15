import threading
import time

def process():
    print("[", end="", flush=True)

    for _ in range(1, 11):
        print("#", end="", flush=True)
        time.sleep(1)

    print("]", end="", flush=True)


def main():
    ex = threading.Thread(target=process, args=())
    
    ex.start()
    ex.join()


if __name__ == "__main__":
    main()
