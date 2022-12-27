
# Solution Link : https://leetcode.com/problems/valid-anagram/submissions/865858168/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        b = t
        for i in s:
            if i in b:
               b = b.replace(i , '', 1)
            else: 
                return False
    
        if b != '':
            return False
        return True