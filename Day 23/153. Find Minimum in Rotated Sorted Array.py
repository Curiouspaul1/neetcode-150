# Solutio Liink :  https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/881596293/
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left, right = 0, len(nums)-1
        
        while left<right:
            mid = (left+right)//2
            if   nums[mid] > nums[right]:
                left = mid +1       
            else:
                right = mid
                
        return nums[left]
            