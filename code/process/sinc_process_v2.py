import multiprocessing


def deposit(balance, lock):
    for _ in range(10000):
        with lock:
            balance.value = balance.value + 1


def withdraw(balance, lock):
    for _ in range(10000):
        with lock:
            balance.value = balance.value - 1


def transaction(balance, lock):
    pc1 = multiprocessing.Process(
        target=deposit,
        args=(
            balance,
            lock,
        ),
    )
    pc2 = multiprocessing.Process(
        target=withdraw,
        args=(
            balance,
            lock,
        ),
    )

    pc1.start()
    pc2.start()

    pc1.join()
    pc2.join()


def main():
    balance = multiprocessing.Value("i", 100)
    lock = (
        multiprocessing.RLock()
    )  # Para resolver o problema de race conditions do ex 1 (Vai sincronizar nosso saldo)

    print(f"Initial Balance: {balance.value}")

    for _ in range(10):
        transaction(balance, lock)

    print(f"Final Balance: {balance.value}")


if __name__ == "__main__":
    main()
