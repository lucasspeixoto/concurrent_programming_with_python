


import multiprocessing


def deposit(balance):
    for _ in range(10000):
        balance.value = balance.value + 1


def withdraw(balance):
    for _ in range(10000):
        balance.value = balance.value - 1
        
def transaction(balance):
    pc1 = multiprocessing.Process(target=deposit, args=(balance,))
    pc2= multiprocessing.Process(target=withdraw, args=(balance,))
    
    pc1.start()
    pc2.start()
    
    pc1.join()
    pc2.join()
    
    
    
def main():
    balance = multiprocessing.Value('i', 100)
    
    print(f'Initial Balance: {balance.value}')
    
    for _ in range(10):
        transaction(balance)
        
    print(f'Final Balance: {balance.value}')


if __name__ == "__main__":
    main()
