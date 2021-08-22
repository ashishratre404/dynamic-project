# Find out Fibonacci 

# 1. Recursion
# def fib(n):
#     if n==0 or n==1:
#         return n
#     return fib(n-1) + fib(n-2)
# print(fib(7))

# 2. DP using memoization
# def fib_mem(n,dp):
#     if n==0 or n==1:
#         return n
#     elif dp[n] != -1:
#         return dp[n]
#     else:
#         dp[n] = fib_mem(n-1, dp) + fib_mem(n-2, dp)
#         return dp[n]

# dp = [-1]*8
# print(fib_mem(7, dp))

# 3. DP using Tabulation
dp = [0]*101
dp[0] = 0
dp[1] = 1
for i in range(2,101):
    dp[i] = dp[i-1] + dp[i-2]
print(dp[7])
print(dp[100])