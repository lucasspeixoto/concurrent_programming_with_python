import threading
import random
import time
import colorama

from typing import List

lock = threading.RLock()


class Account:
    def __init__(self, balance=0) -> None:
        self.balance = balance


def main():
    accounts = create_account()
    
    with lock:
        total = sum(account.balance for account in accounts)
        
    print(colorama.Fore.WHITE + f"Starting transfers...", flush=True)

    tasks = [
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
        threading.Thread(target=services, args=(accounts, total)),
    ]

    [task.start() for task in tasks]

    [task.join() for task in tasks]

    print(colorama.Fore.GREEN + f"Complete transfers...", flush=True)

    valid_bank(accounts, total)


def services(accounts: List[Account], total: int) -> None:
    for _ in range(1, 500):
        c1, c2 = get_two_accounts(accounts)

        value = random.randint(1, 100)

        transfer(c1, c2, value)

        valid_bank(accounts, total)


def create_account() -> List[Account]:

    return [
        Account(balance=random.randint(5000, 10000)),
        Account(balance=random.randint(5000, 10000)),
        Account(balance=random.randint(5000, 10000)),
        Account(balance=random.randint(5000, 10000)),
        Account(balance=random.randint(5000, 10000)),
        Account(balance=random.randint(5000, 10000)),
    ]


def transfer(origem: Account, destiny: Account, value: int) -> None:

    if origem.balance < value:
        return
    
    with lock:
        origem.balance -= value
        time.sleep(0.001)
        destiny.balance += value


def valid_bank(accounts: List[Account], total: int) -> None:
    with lock:
        actual = sum(account.balance for account in accounts)

    if actual != total:
        print(
            colorama.Fore.RED
            + f"Error, balance inconsistence. BRL$ {actual:.2f} x {total:.2f}",
            flush=True,
        )
    else:
        print(colorama.Fore.BLUE + f"Nice. BRL$ {total:.2f}", flush=True)


def get_two_accounts(accounts: List[Account]) -> None:
    c1 = random.choice(accounts)
    c2 = random.choice(accounts)

    while c1 == c2:
        c2 = random.choice(accounts)

    return c1, c2


if __name__ == "__main__":
    main()
