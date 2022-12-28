class Solution:
    def twoSum(self, nums: List[int], target: int):

        for i in range(len(nums)):
            num = nums[i]
            remaining = nums[i + 1:]

            if target - num in remaining:
                return [i, remaining.index(target - num) + i + 1]
