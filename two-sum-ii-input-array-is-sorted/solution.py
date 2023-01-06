class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        r,l=0, len(numbers)-1
        while r < l:
            cursum=numbers[r] + numbers[l]
            if cursum > target:
                l=l-1
            elif cursum < target:
                r=r+1
            else:
                return [r+1,l+1]
 