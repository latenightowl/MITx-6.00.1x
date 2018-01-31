#Write a function that returns the greatest common denominator!

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == b:
        gcd = a
        return gcd
    elif a > b:
        gcd = b
        while gcd > 0:
            if a%gcd == 0:
                if b%gcd == 0:
                    return gcd
            gcd -= 1
    else:
        gcd = a
        while gcd > 0:
            if b%gcd == 0:
                if a%gcd == 0:
                    return gcd
            gcd -= 1    


#Now write a recursive function that returns the gcd!

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
