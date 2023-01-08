class Solution:
    def maxArea(self, height: List[int]) -> int:
        min_index = 0
        max_index = len(height) - 1
        max_area = 0

        for _ in height:
            if height[min_index] < height[max_index]:
                max_area = max(max_area, height[min_index] * (max_index - min_index))
                min_index += 1
            elif height[min_index] >= height[max_index]:
                max_area = max(max_area, height[max_index] * (max_index - min_index))
                max_index -= 1
        return max_area