import threading
import time

def main():
    
    threads = [
        threading.Thread(target=count, args=("elefant", 10)),
        threading.Thread(target=count, args=("bird", 8)),
        threading.Thread(target=count, args=("lion", 23)),
        threading.Thread(target=count, args=("monkey", 12))
    ]
    
    """ 
    # Adiciona a thread no pool de threads prontas
    # para execução.
    """
    [thread.start() for thread in threads]

    print("Running..." * 2)

    """ 
    # Avisa para ficar aguardando aqui até a thread 
    # terminar a execução (Só passa para próxima 
    # linha ao finalizar a função count).
    """
    [thread.join() for thread in threads]

    print("Pronto")


def count(what: str, number: int) -> None:
    for i in range(1, number + 1):
        print(f"{i} {what}s...")
        
        time.sleep(1)


if __name__ == "__main__":
    main()

""" 
# A ordem de execução das threads é decidida pelo
# algoritmo de escalonamento
"""
