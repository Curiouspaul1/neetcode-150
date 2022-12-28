# Solution Link: https://leetcode.com/problems/two-sum/submissions/867132105/

class Solution:
    def twoSum(self, nums, target: int):
        mp = {}
        for i in range(len(nums)):
            if nums[i] not in mp:
                mp[target - nums[i]] = i 
            else:
                return mp[nums[i]], i 

        return -1, -1