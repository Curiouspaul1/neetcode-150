# Solution link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/872223848/

class Solution:
    def twoSum(self, numbers, target):
        start,end = 0, len(numbers)-1
        while start<=end:
            sums = numbers[start]+numbers[end]
            if(sums == target):
                return [start+1, end+1]
            if(sums < target):
                start+=1
            else:
                end-=1
        return [start+1,end+1]