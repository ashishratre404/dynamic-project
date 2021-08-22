# leetcode: 121. Best time to buy and sell stock

def maxprofit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit

print(maxprofit([7,1,5,6,4,3]))