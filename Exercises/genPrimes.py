#Write a function that returns the sequence of prime numbers on #successive calls to its next() method.

def genPrimes():
    primes = []   # list of primes
    x = 1         # candidate number
    while True:
        x += 1
        for p in primes:
            if x % p == 0:
                break
        else:
            primes.append(x)
            yield x