def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[i - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp
        gap //= 2
    return arr


# Пример использования
numbers = [12, 34, 54, 2, 3]
sorted_numbers = shell_sort(numbers)
print(sorted_numbers)
numbers_2 = [10, 7, 8, 9]
sorted_numbers_2 = shell_sort(numbers_2)
print(f"Исходный массив: {numbers_2}",f"Отсортированный массив: {sorted_numbers_2}")
numbers_3 = [1]
sorted_numbers_3 = shell_sort(numbers_3)
print(f"Исходный массив: {numbers_3}",f"Отсортированный массив: {sorted_numbers_3}")
numbers_4 = [3, 3, 3, 2, 2]
sorted_numbers_4 = shell_sort(numbers_4)
print(f"Исходный массив: {numbers_4}",f"Отсортированный массив: {sorted_numbers_4}")
numbers_5 = []
sorted_numbers_5 = shell_sort(numbers_5)
print(f"Исходный массив: {numbers_5}",f"Отсортированный массив: {sorted_numbers_5}")


