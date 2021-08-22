# Leetcode: 300. Longest Increasing Subsequence

def LIS(nums):
    LIS = [1]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], 1+LIS[j])
    return max(LIS)

print(LIS([1,2,4,3]))
