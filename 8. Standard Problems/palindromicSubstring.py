# Leetcode: 647. Palindromic Substring


#Normal approach
def countSubstring(s):
    res = 0

    for i in range(len(s)):
        #for odd lenght substring
        l =i
        r = i
        while l>=0 and r<len(s) and s[l]==s[r]:
            res += 1
            l -= 1
            r += 1
        
        #for even length
        l = i
        r = i+1
        while l>=0 and r<len(s) and s[l] == s[r]:  
            res += 1
            l -= 1
            r += 1
    return res

print(countSubstring('abc'))

# DP Approach
