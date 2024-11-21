from math import gcd
from functools import reduce


def divide_pot(rounds_to_win, wins):
    n = len(wins)
    remaining_rounds = [rounds_to_win - w for w in wins]

    total_remaining = sum(remaining_rounds)

    fractions = [total_remaining - r for r in remaining_rounds]

    common_divisor = reduce(gcd, fractions)
    result = [f // common_divisor for f in fractions]

    return result



print(divide_pot(3, [2, 1]))
print(divide_pot(5, [1, 1, 2])) 
