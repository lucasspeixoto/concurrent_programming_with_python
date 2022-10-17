import datetime

import comput

def main():

    start: datetime.datetime = datetime.datetime.now()
     
    comput.compute(end=50000000)
 
    time: datetime.timedelta = datetime.datetime.now() - start

    print(f"Cython Finish in {time.total_seconds()} s")


if __name__ == "__main__":
    main()
