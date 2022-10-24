"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def isPrime(num):
    x = int(num)
    if x ==1:
        return 0
    elif x==2:
        return 1
    for i in range(2,round(x/2)+1):
        if x%i==0:
            return 0
        elif x % i !=0:
            if i == round(x/2):
                return 1




def primes(number_of_primes):
    list = []
    n =int(number_of_primes)
    if n<=0:
        raise ValueError("error")
    y = 0
    prime_counter = 0
    while prime_counter<=n-1:
        if isPrime(y) ==1:
            list.append(y)
            prime_counter +=1
        y +=1
    return list
