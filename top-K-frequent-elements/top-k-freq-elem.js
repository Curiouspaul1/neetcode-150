var topKFrequent = function(nums, k) {
    let frequencyObj = {};
    let result = [];
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in frequencyObj) {
            frequencyObj[nums[i]]++;
        } else {
            frequencyObj[nums[i]] = 1;
        }
    }
    let sorted = Object.keys(frequencyObj).sort((a, b) => frequencyObj[b] - frequencyObj[a]);
    for (let i = 0; i < k; i++) {
        result.push(sorted[i]);
    }
    return result;
};
console.log(topKFrequent([1,1,1,2,2,3], 2));
console.log(topKFrequent([1], 1));
