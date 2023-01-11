class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_substr = set()
        result = 0
        l = 0
        for k, v in enumerate(s):
            while v in unique_substr:
                unique_substr.remove(s[l])
                l += 1
            unique_substr.add(v)
            result = max(result, k-l+1)
        return result