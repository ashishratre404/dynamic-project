# Leetcode: 198. House Robber

def rob(nums):
    rob1, rob2 = 0, 0

    # [rob1, rob2, n, n-1,.....]
    for n in nums:
        temp = max(n + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2
print(rob([1,21,3,4]))


#how its working
# rob1, rob2 = 0, 0
# [1,2,3,1]

# n = 1
