# Solution Link: https://leetcode.com/problems/trapping-rain-water/description/
class Solution:
    def trap(self, height):
        maxL = 0 
        maxR = 0
        ans = 0

        l, r = 0, len(height) - 1
        while l < r:
            if height[l] > height[r]:
                maxR = max(maxR, height[r])
                ans = ans + (maxR - height[r])
                r -= 1
            elif height[l] <= height[r]:
                maxL = max(maxL, height[l]) 
                ans = ans + (maxL - height[l])
                l += 1 

        return ans