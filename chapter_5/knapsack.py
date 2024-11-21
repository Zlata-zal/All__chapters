def knapsack(items, weight_limit):
    dp = [0] * (weight_limit + 1)

    for weight, value in items:
        for w in range(weight_limit, weight - 1, -1):
            dp[w] = max(dp[w], dp[w - weight] + value)

    return dp[weight_limit]


items_1 = [(2, 10), (3, 15), (5, 30)]
weight_limit_1 = 5
print(knapsack(items_1, weight_limit_1))

items_2 = [(2, 10), (3, 15), (5, 30), (7, 20), (1, 5), (4, 10)]
weight_limit_2 = 10
print(knapsack(items_2, weight_limit_2))

items_3 = [(2, 20), (3, 15), (5, 30), (1, 25), (4, 10)]
weight_limit_3 = 7
print(knapsack(items_3, weight_limit_3))

items_4 = [(2, 5), (3, 8), (5, 15), (1, 3), (4, 10)]
weight_limit_4 = 7
print(knapsack(items_4, weight_limit_4))

items_5 = [(6, 10), (8, 15), (12, 30)]
weight_limit_5 = 5
print(knapsack(items_5, weight_limit_5))