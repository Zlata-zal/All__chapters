def max_profit(prices):
    min_price = prices[0]
    max_profit = 0
    buy_day = 0
    sell_day = 0

    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
            buy_day = i
        profit = prices[i] - min_price
        if profit > max_profit:
            max_profit = profit
            sell_day = i

    return max_profit, buy_day, sell_day

gold_prices_1 = [100, 120, 140, 160, 180, 200, 220]
gold_prices_2 = [200, 180, 220, 160, 240, 260, 210]
gold_prices_3 = [250, 230, 210, 190, 170, 150, 130]
gold_prices_4 = [200, 200, 200, 200, 200, 200, 200]
gold_prices_5 = [150, 160, 155, 170, 180, 175, 165]
for prices in [gold_prices_1]:
    profit, buy, sell = max_profit(prices)
    if profit > 0:
        print(f"Максимальная прибыль: {profit}, купить на день {buy + 1}, продать на день {sell + 1}")
    else:
        print("Прибыль невозможна")