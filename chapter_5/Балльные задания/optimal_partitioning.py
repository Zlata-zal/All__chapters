import math
from collections import Counter

def factorize(n):
    factors = []
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i
    if n > 1:
        factors.append(n)
    return factors

def compute_score(partition):
    counter = Counter(partition)
    unique_factors = list(counter.keys())
    k = len(unique_factors)
    sc = sum(d * f for d, f in counter.items()) * k
    return sc

def find_spec_prod_part(n, com):
    factors = factorize(n)

    if com == 'max':
        partition = sorted(factors, reverse=True)
    elif com == 'min':
        partition = sorted(factors)

    score = compute_score(partition)

    return [partition, score]

print(find_spec_prod_part(1416, 'max'))
print(find_spec_prod_part(1416, 'min'))