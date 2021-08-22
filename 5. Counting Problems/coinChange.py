# Leetcode: 322. Coin Change

def coinChange(coins, amount):
    dp = [amount+1]*(amount + 1)
    dp[0] = 0

    for a in range(1, amount+1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1+dp[a-c])
                print(dp)
    return dp[amount] if dp[amount] != amount+1 else -1

print(coinChange([1,2,5],11))


#solution
#  dp = [0,12,12,12,12,12,12,12,12,12,12,12]

#  a=1
#  c = 1
#  dp= [0,1,12,12................]

#  a=2
#  c=1
#  dp=[0,1,2,12,12.............]

#  a=2
#  c=2
#  dp=[0,1,1,.................]

#  a=3
#  c=1
#  dp=[0,1,1,2,....]

#  a=3
#  c=2
#  dp=[0,1,1,2,12,...........]

# a=4
# c=1
# dp=[0,1,1,2,3,.......]

# a=4
# c=2
# dp=[0,1,1,2,2.......]

# a=5
# c=1
# dp=[0,1,1,2,2,3......]

# a=5
# c=2
# dp=[0,1,1,2,2,3......]

# a=5
# c=5
# dp=[0,1,1,2,2,1......]

# .
# .
# .
# .
# .
# a = 11
# c = 5
# dp = [0,1,1,2,2,1,2,2,3,3,2,3]
