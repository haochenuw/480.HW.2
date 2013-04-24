from operator import add
def det3(a):
   x = (a[0][0] * a[1][1] * a[2][2]) + (a[1][0] * a[2][1] * a[0][2]) + (a[2][0] * a[0][1] * a[1][2])
   y = (a[0][2] * a[1][1] * a[2][0]) + (a[1][2] * a[2][1] * a[0][0]) + (a[2][2] * a[0][1] * a[1][0])
   return x - y
def det4(a):
    result = 1 
    b = [[]]*3
    for n in range(4):
        if a[n][0] != 0: break
    a[0],a[n] = a[n],a[0]
    result *= (-1)**n
    for n in range(1,4):
        b[n-1] = map(add, a[n],[-x*a[n][0]/a[0][0] for x in a[0]])[1:]
    return result*det3(b)

%cython
cimport numpy as numpy
ctypedef numpy.float64_t DTYPE_t
from operator import add
def det3(numpy.ndarray[DTYPE_t,ndim =2] a):
    cdef DTYPE_t x = (a[0][0] * a[1][1] * a[2][2]) + (a[1][0] * a[2][1] * a[0][2]) + (a[2][0] * a[0][1] * a[1][2])
    cdef DTYPE_t y = (a[0][2] * a[1][1] * a[2][0]) + (a[1][2] * a[2][1] * a[0][0]) + (a[2][2] * a[0][1] * a[1][0])
    return x - y
def det4(a):
    cdef DTYPE_t result = 1 
    b = [[]]*3
    cdef int n
    for n in range(4):
        if a[n][0] != 0: break
    a[0],a[n] = a[n],a[0]
    result *= (-1)**n
    cdef int m
    for m in range(1,4):
        b[m-1] = map(add, a[m],[-x*a[m][0]/a[0][0] for x in a[0]])[1:]
    return result*det3(b)


# multiplication of two 4 by 4 matrices: 

def mult(a,b):
  return a*b


%cython
cimport numpy as np
def mult(np.matrix a,  np.matrix b):
    return a*b

#Note: I got an error with this definition, saying that 'matrix' is not a type identifier,
no idea what's wrong 








