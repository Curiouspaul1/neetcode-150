# Solution Link: https://leetcode.com/problems/top-k-frequent-elements/submissions/868264083/


class Solution:
    def topKFrequent(self, nums, k: int):
        mem = {}
        for i in nums:
            if i in mem: mem[i] += 1
            else: mem[i] = 1
        nums = list(set(nums))
        nums.sort(key=lambda x: mem[x], reverse=True)
        return nums[0:k]