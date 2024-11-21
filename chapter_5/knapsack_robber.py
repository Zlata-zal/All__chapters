def knapsack(items, time_limit, weight_limit):
    dp = [[0] * (weight_limit + 1) for _ in range(time_limit + 1)]

    for value, time, weight in items:

        for t in range(time_limit, time - 1, -1):
            for w in range(weight_limit, weight - 1, -1):
                dp[t][w] = max(dp[t][w], dp[t - time][w - weight] + value)

    return dp[time_limit][weight_limit]


items_1 = [(10, 5, 2), (15, 4, 3), (30, 7, 5)]
time_limit_1 = 10
weight_limit_1 = 10

items_2 = [(20, 6, 4), (15, 3, 3), (25, 5, 5), (10, 2, 2), (12, 4, 3)]
time_limit_2 = 12
weight_limit_2 = 10

items_3 = [(15, 5, 3), (12, 4, 2), (30, 7, 5), (25, 6, 4), (20, 3, 3)]
time_limit_3 = 15
weight_limit_3 = 12

items_4 = [(10, 4, 2), (20, 5, 3), (15, 3, 2), (25, 6, 4), (18, 4, 3)]
time_limit_4 = 13
weight_limit_4 = 11