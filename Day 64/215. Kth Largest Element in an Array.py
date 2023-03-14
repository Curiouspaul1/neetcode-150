import heapq
# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/914905535/

class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return(nums[0])