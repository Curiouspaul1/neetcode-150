/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
  let lookUp = {};
  let result = [];
  nums.forEach(item => {
    if (!lookUp[item]) lookUp[item] = 0;
    lookUp[item]++;
  });
  let sortedArr = Object.entries(lookUp).sort((a, b) => b[1] - a[1]);
  for (let i = 0; i < k; i++) {
    result.push(sortedArr[i][0]);
  }
  return result;
};
