class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums and len(nums) < 3:
            return []
        result = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.twoSum(nums, i, result)
        return result
                
    def twoSum(self, nums: List[int], i: int, result: List[List[int]]):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                result.append([nums[i], nums[left], nums[right]])
                left += 1
                right -= 1
                
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1