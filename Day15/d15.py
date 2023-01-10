def longestSubstring(s):

    #code here
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l +=1
        charSet.add(s[r])
        res = max(res, charSet.__len__())

    return res


s ="abcabcbb"
print(longestSubstring(s))