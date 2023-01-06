class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, j in enumerate(nums):
            if i > 0 and j == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = j + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    result.append([j, nums[r], nums[l]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return result
