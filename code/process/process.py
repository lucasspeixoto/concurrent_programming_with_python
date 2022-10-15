import multiprocessing

def do_something(value: str):
    print("Doing something with the {}".format(value))


def main():
    
    print(f"Starting with the process: {multiprocessing.current_process().name}")
    
    pc = multiprocessing.Process(
        target=do_something, args=("Car",), name="Do Something"
    )

    print(f"Starting with the process: {pc.name}")

    pc.start()

    pc.join()

    return


if __name__ == "__main__":
    main()
