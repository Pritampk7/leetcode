prices = [10, 9, 3, 8, 6]
output = 5


def stock(prices):
    buy = 0
    currentProfit = 0
    for sell in range(len(prices)):
        if prices[buy] < prices[sell]:
            profit = prices[sell] - prices[buy]
            currentProfit = max(currentProfit, profit)
        else:
            buy = sell
        sell += 1
    return currentProfit


print(stock(prices))
