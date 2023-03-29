'''

Write a function primes which generates a list of primes up to n. 
Implement is_prime function that determines if a number is prime and
then using it to filter non-primes.
def is_prime(m : int) -> bool:
pass
def primes(n : int) -> List[int]:
pass
>>> primes(10)
[2, 3, 5, 7]
>>> primes(1)
[]

'''

def is_prime(m):
    if m == 1:
        return False
    elif m ==2:
        return True
    else:
        for i in range(2,m):
            if m%i==0:
                return False
    return True
    
def primes(n):
    primelist = []
    for i in range(1,n):
        if is_prime(i):
            primelist.append(i)
    return primelist


