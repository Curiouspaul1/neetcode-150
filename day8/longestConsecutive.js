/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
  if (nums.length === 0) return 0;

  let sorted = nums.sort((a, b) => a - b);
  let diff = 0;
  let count = {};
  
  let current = 0;
  for (let i = 0; i < nums.length; i++) {
    diff = sorted[i+1] - sorted[i];
    if (diff === 0) continue;
    if (!count[current]) count[current] = 0;
    count[current]++;
    if (diff > 1) current = i + 1;
  }
  return Object.values(count).sort((a, b) => b - a)[0];
};