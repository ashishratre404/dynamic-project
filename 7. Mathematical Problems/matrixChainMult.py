
# Aim: Find a most efficient way to multiply a sequence of matrices

# for example
#  we have three matrices:   A: 5X20   B: 20X10  C: 10X50
#  and we have to compute: ABC

#  so we have two options:
#     1. (AB)C   : 50X20X10 + %X10X50 =  3500 operations
#     2. A(BC) :  20X10X50 + 5X20X50   =  15000 oprations

# thus we can say, option 1 is more efficient than option 2

def mcm(d):
    n = len(d)-1
    m = {(i,j): float('inf') for i in range(1,n+1) for j in range(i,n+1)}

    for i in range(n, n+1):
        m[(i,i)] = 0
    
    for i in range(1,n+1):
        for j in range(i, n+1):
            if i == j:
                m[(i,j)] = 0
            else:
                m[(i,j)] = min(m[(i,j)] + m[(k+1,j)] + d[i-1]*d[k]*d[j] for k in range(i,j))
    return m[(1,n)]

d = [5,20,10,50]
print(mcm(d))
