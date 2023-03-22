def partition(s):
    if not s:
        return []
    res = []
    dfs(s, [], res)
    return res

def dfs(s, path, res):
    if not s:
        res.append(path)
        return
    for i in range(1, len(s) + 1):
        if isPalindrome(s[:i]):
            dfs(s[i:], path + [s[:i]], res)


def isPalindrome(s):
    return s == s[::-1]


