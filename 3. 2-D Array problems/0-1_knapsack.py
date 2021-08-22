# Weight ->  1, 2, 4, 2, 5
# Value ->   5, 3, 5, 3, 2
# n-> no. of items, c-> capacity we have

#Recursive solution
# def ks_recursive(n,c,w,v):
#     if n ==0 or c==0:
#         result = 0
#     elif w[n] >c:
#         result = ks_recursive(n-1,c)
#     else:
#         tepm1 = ks_recursive(n-1, c-w[n])
#         temp2 = v[n] + ks_recursive(n-1,c-w[n])
#         result = max(tepm1, temp2)
#     return result

#memoization
# arr[n][c] = undefined
# def ks_memoization(n,c,w,v):
#     if arr[n][c] != undefiend: return arr[n][c]
#     if n ==0 or c==0:
#         result = 0
#     elif w[n] >c:
#         result = ks_recursive(n-1,c)
#     else:
#         tepm1 = ks_recursive(n-1, c-w[n])
#         temp2 = v[n] + ks_recursive(n-1,c-w[n])
#         result = max(tepm1, temp2)
#     arr[n][c] = return
#     return result