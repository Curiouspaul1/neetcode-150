# Solution Link : https://leetcode.com/problems/contains-duplicate/submissions/865751912/

class Solution:
    def containsDuplicate(self, nums):
        elem = {}
        for i in nums:
            if i in elem:
                return True
            elem[i] = i
        return False