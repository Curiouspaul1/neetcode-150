

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        n = len(nums)
        if n == 0:
            return answer
        if k > len(nums):
            return [max(nums)]
        # Pre allocate list with final answer size
        answer = [0] * (n - k + 1)
        window = deque()
        iter = 0
        # Iterate over first k to fill the deque
        for i in range(k):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
        answer[iter] = nums[window[0]]
        iter += 1
        # iterate over rest of List
        for i in range(k, len(nums)):
            # Pop deque when current number >= top of deque
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            # When deque size > window k, pop leftmost element
            if window and window[0] <= (i - k):
                window.popleft()
            window.append(i)
            answer[iter] = nums[window[0]]
            iter += 1
        return answer
