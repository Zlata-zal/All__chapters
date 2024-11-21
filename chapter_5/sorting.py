import random
import time
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def generate_random_list(length):
    return [random.randint(1, 1000) for _ in range(length)]

def test():
    for size in [100, 1000, 10000, 100000]:
        arr = generate_random_list(size)

        start_time = time.time()
        merge_sort(arr.copy())
        merge_sort_time = time.time() - start_time

        start_time = time.time()
        selection_sort(arr.copy())
        selection_sort_time = time.time() - start_time

        print(f"Размер списка: {size}")
        print(f"Время выполнения сортировки слиянием: {merge_sort_time:.5f} сек")
        print(f"Время выполнения сортировки выбором: {selection_sort_time:.5f} сек")
        print("=" * 50)


if __name__ == "__main__":
    test()
