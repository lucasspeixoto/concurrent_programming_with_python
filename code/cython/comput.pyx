import cython
from libc.math cimport sqrt

def compute(end: cython.int, start: cython.int=1):
    pos: cython.int = start

    factor: cython.int = 1000 * 1000

    with nogil:
        while pos < end:
            pos += 1
            sqrt((pos - factor) * (pos - factor))
