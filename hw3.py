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
