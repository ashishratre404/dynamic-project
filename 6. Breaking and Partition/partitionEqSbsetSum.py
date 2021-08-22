# Leetcode 416.Partition Equal Subset Sum


def canPartition(nums):
    if sum(nums)%2: return False

    dp = set()
    dp.add(0)
    target = sum(nums)//2

    for i in range(len(nums)):
        nextDp = set()
        for t in dp:
            nextDp.add(t + nums[i])
            nextDp.add(t)
        dp = nextDp
    return True if target in dp else False

print(canPartition([11,22,1,12]))

     