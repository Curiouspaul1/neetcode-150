# Solution Link: https://leetcode.com/problems/product-of-array-except-self/submissions/868961129/

class Solution:
    def productExceptSelf(self, nums):
       
        res = [1]*(len(nums))
        left_pass = 1
        right_pass = 1
        for i in range(len(nums)):
            res[i] = left_pass
            left_pass *=nums[i]

        for i in range(len(nums)-1, -1,-1):
            res[i] *= right_pass
            right_pass  *=nums[i] 

        return res