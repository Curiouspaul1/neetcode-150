import 'dart:math' as math;

class Solution {
 int maxArea(List<int> height) {
  // Create a variable to store the max area
  int max = 0;
  // Create two pointers
  int left = 0;
  int right = height.length - 1;
  // Iterate through the array
  while (left < right) {
    // Update the max area
    max = math.max(max, (right - left) * math.min(height[left], height[right]));
    // Move the pointer with the smaller height
    if (height[left] < height[right]) {
      // Move the left pointer to the right
      left++;
    } else {
      // Move the right pointer to the left
      right--;
    }
  }

  return max;
}

}