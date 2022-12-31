class Solution:
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        
        prefix = 1
        
        for x in range(len(nums)):
            res[x] = prefix
            prefix *= nums[x]

        suffix =1

        for x in range(len(nums) -1 , -1, -1):
            res[x] *= suffix
            suffix *= nums[x]
                
        return res
                