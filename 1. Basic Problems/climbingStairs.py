# leetcode: 70. Climbing Stairs

lastStep, secondlastStep = 1, 1
# here n=5,so we have to calculate for total 6 steps that is 0,1,2,3,4,5, but we have already done for two steps
# so, we will loop over n-1 that is 5-1 = 4
for i in range(5-1): 
    # calculating for next step that is sum of last two
    # we are shifting lastStep and secondlastStep to one postion down 
    # that means now, secondlastSteps becomes lastStep and then recently calculated becomes secondlastStep 
    nextStep = lastStep + secondlastStep
    lastStep = secondlastStep
    secondlastStep = nextStep
print(secondlastStep)


# How it is happening

# we have n=5
# so
# 0(ground level), 1, 2, 3, 4 (secondlastStep), 5 (lastStep)

# lastStep       = 5 and  value = 1
# secondlastStep = 4 and value = 1

# first iteration, i = 0
# nextStep = 3 and value = 1+1 = 2
# lastStep = 4 and value = 1
# secondlastStep = 3 and value = 1+1 = 2

# first iteration, i = 1
# nextStep = 2 and value = 1+2 = 3
# lastStep = 3 and value = 2
# secondlastStep = 2 and value = 1+2 = 3

# first iteration, i = 2
# nextStep = 1 and value = 2+3 = 5
# lastStep = 2 and value = 3
# secondlastStep = 1 and value = 2+3 = 5

# first iteration, i = 3
# nextStep = 0 and value = 3+5 = 8
# lastStep = 1 and value = 5
# secondlastStep = 0 and value = 3+5 = 8

# now 
# print(secondlastStep)  --> 8