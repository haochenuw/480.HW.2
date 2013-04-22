def sum_squares(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum
    
timeit('sum_squares(10000)')

%cython
def sum_squares1(int n):
    result = []
    cdef int sum, i = 0
    for i in range(1,n+1):
        sum += i**2
    return sum
    
timeit('sum_squares1(10000)')


import floor from math

def list_primes(X):
    """
    computes a list of primes up to X
    """
    list = range(2,X+1)
    for n in range(2,floor(X**0.5)+1):
        list = [m for m in list if m%n != 0 or m==n]
    return list
    
%cython
cdef extern from "math.h":
    cdef int floor(double)

def list_primes1(X):
    """
    computes a list of primes up to X
    """
    result =[]
    cdef n,m = 0
    for n in range(2,X):
        for m in range(2,floor(m**0.5)+1):
            check = True
            if n%m == 0 and n != m: 
                check = False
                break
        if check:
            result.append(n)
    return result
