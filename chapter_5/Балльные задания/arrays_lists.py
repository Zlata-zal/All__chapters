import itertools

def gta(limit, *numbers):
    digits_set = set()
    for num in numbers:
        digits_set.update(str(num))

    sorted_digits = sorted(int(digit) for digit in digits_set)

    base_list = sorted_digits[:limit]

    total_sum = 0
    for length in range(1, len(base_list) + 1):
        for combination in itertools.permutations(base_list, length):
            total_sum += sum(combination)

    return total_sum

print(gta(7, 123489, 5, 67))

print(gta(8, 12348, 47, 3639))
