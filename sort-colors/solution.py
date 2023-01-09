class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l,r=0, len(nums)-1
        i=0
        while i<=r:
            if nums[i]==0:
                temp=nums[l]
                nums[l]=nums[i]
                nums[i]=temp
                l=l+1
            elif nums[i]==2:
                temp=nums[r]
                nums[r]=nums[i]
                nums[i]=temp
                r=r-1
                i=i-1
            i=i+1
        return nums
            
                
