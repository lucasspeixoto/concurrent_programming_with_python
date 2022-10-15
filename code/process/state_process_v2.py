import multiprocessing
import time
import ctypes

""" 
Aqui os dados 
"""


def function1(value: int, state: bool):

    if state.value:
        result = value.value + 10
        state.value = False
    else:
        result = value.value + 20
        value.value = 200
        state.value = True

    print(f"Function 1 Result: {result}")
    time.sleep(0.001)


def function2(value: int, state: bool):

    if state.value:
        result = value.value + 30
        state.value = False
    else:
        result = value.value + 40
        value.value = 400
        state.value = True

    print(f"Function 2 Result: {result}")
    time.sleep(0.001)


def main():
    value = multiprocessing.Value('i', 100)

    state = multiprocessing.Value(ctypes.c_bool, False)

    p1 = multiprocessing.Process(target=function1, args=(value, state))
    p2 = multiprocessing.Process(target=function2, args=(value, state))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
