/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
  let n = nums.length;
  let result = new Array(n).fill(1);
  for (let i = 1; i < n; i++) {
    result[i] = result[i - 1] * nums[i - 1];
  }
  let pRight = nums[n - 1];
  for (let i = n - 2; i >= 0; i--) {
    result[i] *= pRight;
    pRight *= nums[i];
  }
  return result;
};