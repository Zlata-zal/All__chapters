
from collections import Counter

def most_frequent_value_count(n, q, array, queries):
    results = []
    for left, right in queries:
        left -= 1
        right -= 1
        freq = Counter(array[left:right + 1])
        max_frequency = max(freq.values())
        results.append(max_frequency)
    return results

def test_most_frequent_value_count():
    n1, q1 = 10, 3
    array1 = [-1, -1, 1, 1, 1, 1, 3, 10, 10, 10]
    queries1 = [(2, 3), (1, 10), (5, 10)]
    expected1 = [1, 4, 3]
    result1 = most_frequent_value_count(n1, q1, array1, queries1)
    print(f"Test 1: {result1} (Expected: {expected1})")
    assert result1 == expected1

    # Тест 2
    n2, q2 = 5, 2
    array2 = [1, 1, 2, 2, 2]
    queries2 = [(1, 5), (2, 4)]
    expected2 = [5, 3]
    result2 = most_frequent_value_count(n2, q2, array2, queries2)
    print(f"Test 2: {result2} (Expected: {expected2})")



    # Тест 3
    n3, q3 = 6, 3
    array3 = [3, 3, 4, 4, 4, 5]
    queries3 = [(1, 2), (1, 6), (3, 6)]
    expected3 = [2, 4, 3]
    result3 = most_frequent_value_count(n3, q3, array3, queries3)
    print(f"Test 3: {result3} (Expected: {expected3})")


    # Тест 4
    n4, q4 = 1, 1
    array4 = [7]
    queries4 = [(1, 1)]
    expected4 = [1]
    result4 = most_frequent_value_count(n4, q4, array4, queries4)
    print(f"Test 4: {result4} (Expected: {expected4})")



    # Тест 5
    n5, q5 = 7, 3
    array5 = [1, 2, 2, 3, 3, 3, 4]
    queries5 = [(1, 7), (2, 5), (3, 7)]
    expected5 = [3, 3, 3]
    result5 = most_frequent_value_count(n5, q5, array5, queries5)
    print(f"Test 5: {result5} (Expected: {expected5})")


    print("All tests passed!")


test_most_frequent_value_count()
