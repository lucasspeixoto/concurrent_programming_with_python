from typing import Generator

"""
Generator é um tipo especial de função onde
podemos ter o controle da execução, executar,
pausar e retomar conforme necessário.

A função não executa e finaliza, ela aguarda a
próxima chamada

"""


def fibo() -> Generator[int, None, None]:

    value: int = 0
    next: int = 1

    while True:
        value, next = next, value + next
        yield value  # Devolve value e aguarda a próxima chamada


if __name__ == "__main__":
    for n in fibo():
        print(n, end=", ")
        if n > 100:
            break

    print("\nReady")
