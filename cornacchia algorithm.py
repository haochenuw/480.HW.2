def find_sol(p,d):
    r"""
    input - a prime p, an absolute value of discriminant d
    output - a solution (x,y) in integers to the equation
    x^2 + d*y^2 = p, if there exist one. 
    """
    if kronecker(-d,p) == 1: 
        t = find_sqrt(p,-d)
        bound = floor(p^(.5))
        n = p
        while(t >= bound):
            n,t = t, n%t
        if ((p-t^2)/d)^(.5) in ZZ:
            return (t, ZZ(((p-t^2)/d)^(.5)))
        else:
            return None
    else:
        return None

def find_sqrt(p,D):
    r"""
    input - a prime p, a quadratic residue m
    output -  a square root of m
    """
    F = GF(p) 
    D = F(D)
    x = PolynomialRing(F,'x').gen()
    f = x^2 - D
    return ZZ(f.roots()[0][0])
    
