class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix=1
        res=[]
        for i in range(len(nums)):
            res.append(prefix)
            prefix=prefix*nums[i]
        postfix=1
        for i in range(len(nums)-1,-1,-1):
            res[i]=res[i]*postfix
            postfix=postfix*nums[i]
        return res


        