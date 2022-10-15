import multiprocessing
import time


def function1(value: int, state: bool):

    if state:
        result = value + 10
        state = False
    else:
        result = value + 20
        value = 200
        state = True

    print(f"Function 1 Result: {result}")
    time.sleep(0.001)


def function2(value: int, state: bool):

    if state:
        result = value + 30
        state = False
    else:
        result = value + 40
        value = 400
        state = True

    print(f"Function 2 Result: {result}")
    time.sleep(0.001)


def main():
    value = 100

    state = False

    p1 = multiprocessing.Process(target=function1, args=(value, state))
    p2 = multiprocessing.Process(target=function2, args=(value, state))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    
if __name__ == '__main__':
    main()
