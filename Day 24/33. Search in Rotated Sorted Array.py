
# https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/914373883/

class Solution:
    def search(self, nums, target: int) -> int:
        count = 0
        if not nums:
            return -1

        for i in nums:

            if i == target:
                return count

            count += 1

        return -1
