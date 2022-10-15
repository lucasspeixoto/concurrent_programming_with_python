import multiprocessing

"""
Em relação ao pipel a Queue da uma maior controle dos processos,
como por exemplo no uso de lock e unlock
"""


def ping(queue):
    queue.put("Lucas")


def pong(queue):
    user_name = queue.get()
    print(f"User name Received: {user_name}")


def main():

    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=ping, args=(queue,))

    p2 = multiprocessing.Process(target=pong, args=(queue,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()


if __name__ == "__main__":
    main()
