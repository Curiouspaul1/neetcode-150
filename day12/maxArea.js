/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
  let l = 0, r = height.length - 1;
  let area = 0;
  let lookUp = [];
  while (l < r) {
    area = Math.min(height[l], height[r]) * (r - l);
    if (height[l] < height[r]) l++;
    else if (height[l] > height[r]) r--;
    else {
        l++,
        r--;
    };
    lookUp.push(area);
  }
  return lookUp.reduce((a, b) => Math.max(a, b), -Infinity);
};
