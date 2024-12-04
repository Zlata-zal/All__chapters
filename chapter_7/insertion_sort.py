def insertion_sort(arr):

    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] == arr[j]
            j -= 1
        arr[j + 1] = current_value

    return arr

examples = [
    [5, 2, 9, 1, 5, 6],
    [10, 7, 8, 9],
    [1],
    [3, 3, 3, 2, 2],
    []
]

for i, example in enumerate(examples, 1):
    print(f"Пример {i}:")
    print(f"Исходный массив: {example}")
    sorted_array = insertion_sort(example.copy())
    print(f"Отсортированный массив: {sorted_array}")