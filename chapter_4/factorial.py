def largest_power_of_prime_in_factorial(n, k):
    exponent = 0
    power = k


    while n // power > 0:
        exponent += n // power
        power *= k

    return exponent


n = 10
k = 2
result = largest_power_of_prime_in_factorial(n, k)
print(f"The largest power of {k} that divides {n}! is {result}")