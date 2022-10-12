import threading
import time

def main():

    thread = threading.Thread(target=count, args=("elefant", 10))

    """ 
    # Adiciona a thread no pool de threads prontas
    # para execução.
    """
    thread.start()

    print("Running..." * 2)

    """ 
    # Avisa para ficar aguardando aqui até a thread 
    # terminar a execução (Só passa para próxima 
    # linha ao finalizar a função count).
    """
    thread.join()
    
    print("Pronto")


def count(what: str, number: int):
    for i in range(1, number + 1):
        print(f"{i} {what}s...")
        
        time.sleep(1)


if __name__ == "__main__":
    main()

"""
Finish in 12.67 s
"""
