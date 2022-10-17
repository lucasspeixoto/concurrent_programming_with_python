import datetime
import comput
import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor
 
 
def main() -> None:
    cores = multiprocessing.cpu_count()
     
    start: datetime.datetime = datetime.datetime.now()
 
    with Executor(max_workers=cores) as executor:
        for n in range(1, cores+1):
            _start = 50000000 * (n - 1) / cores
            _end = 50000000 * n / cores
            executor.submit(comput.compute, start=_start, end=_end)
 
    time: datetime.timedelta = datetime.datetime.now() - start
 
    print(f'Cython with multiprocessing Finish in {time.total_seconds():.2f} s')
 
 
if __name__ == '__main__':
    main()