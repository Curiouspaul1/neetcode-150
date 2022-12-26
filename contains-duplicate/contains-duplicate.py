class Solution:
    def containsDuplicate(self, nums: List[int]):
        left, right = 0, 1

        nums = sorted(nums)
        nums_len = len(nums)

        if nums_len == 1 or nums_len == 0:
            return False

        while right < nums_len:
            if nums[left] == nums[right]:
                return True

            left += 1
            right += 1

        return False
