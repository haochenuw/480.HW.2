%cython
def find_sol(int p,int d):
    r"""
    input - a prime p, an absolute value of discriminant d
    output - a primitive solution (x,y) in integers to the equation
    x^2 + d*y^2 = p, if there exist one, otherwise return none.
    example:
    sage: find_sol(5,1) 
    sage: (2,1)
    """
    if kronecker(-d,p) == 1: 
        cdef int t = find_sqrt(p,-d)
        cdef double bound = p^(.5)
        cdef int n = p
        while True:
            n,t = t, n%t
            if t < bound: break
        if ((p-t^2)/d)^(.5) in ZZ:
            return (t, ZZ(((p-t^2)/d)^(.5)))
        else:
            return None
    else:
        return None

def int find_sqrt(int p,int D):
    r"""
    input - a prime p, a quadratic residue D
    output -  one square root of D in the finite field GF(p)
    example:
    sage: find_sqrt(5,4)
    sage: 3
    """
    F = GF(p) 
    D = F(D)
    x = PolynomialRing(F,'x').gen()
    try: 
        cdef int f = x^2 - D
        return ZZ(f.roots()[0][0])
    except Exception, err:
        print "error: "+ str(D) + " is not a quadratic residue mod " + str(p)
