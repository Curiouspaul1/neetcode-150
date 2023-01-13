/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var maxSlidingWindow = function(nums, k) {
  const dequeue = []; 
  const output = [];
  
  for (let i = 0; i < nums.length; i++) {
    while (nums[i] > dequeue[dequeue.length - 1]) {
      dequeue.pop();
    }
    
    dequeue.push(nums[i]);
    if (i >= k - 1) {
      output.push(dequeue[0]);
      if (nums[i - k + 1] === dequeue[0]) {
        dequeue.shift();
      }
    }
  }
  
  return output;
};