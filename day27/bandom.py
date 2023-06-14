import numpy as np


def pirminis(num):
    if num < 2:
        return False
    for i in range(2, int(np.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


vektorius = np.arange(1, 101)
vectorized_is_prime = np.vectorize(pirminis)
primes = vectorized_is_prime(vektorius)
primes_vector = vektorius[primes]
print(primes_vector)
