/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  let l = 0, r = height.length - 1;
  let area = Math.min(height[l], height[r]) * (r - l);
  let maxArea = area;
  while (r > l) {
    area = Math.min(height[l], height[r]) * (r - l);
    if (height[l] < height[r]) l++;
    else if (height[l] > height[r]) r--;
    else { l++; r-- }
    if (area > maxArea) maxArea = area;
  }
  return maxArea;
};