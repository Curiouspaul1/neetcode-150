# Solution Link: https://leetcode.com/problems/longest-consecutive-sequence/submissions/870710081/

class Solution:
    def longestConsecutive(self, nums) -> int:
        arr = []
        count = 0
        res = 1
        if len(nums) ==0:
            return 0
        nums.sort()


        for i in range(len(nums)):
            if nums[i] != nums[i-1] :
                arr.append(nums[i])

        for i in range(len(arr)):

            if i>0 and arr[i] ==arr[i-1] +1:
                count +=1
            else:
                count = 1
            res = max(count, res)


        return res