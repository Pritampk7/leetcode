prices = [10, 9, 3, 8, 6]
output = 5


def stock(prices):
    buy = 0
    maxPrice = 0
    for sell in range(len(prices)):
        if prices[buy] < prices[sell]:
            total = prices[sell] - prices[buy]
            maxPrice = max(maxPrice, total)
        else:
            buy = sell
        sell += 1
    return maxPrice


print(stock(prices))