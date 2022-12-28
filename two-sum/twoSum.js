var twoSum = function(nums, target) {
    let output = [];
    nums.forEach((currentItem, currentIndex)=> {
        for(let i = currentIndex + 1; i < nums.length; i++) {
            if(currentItem + nums[i] === target) {
                output.push(currentIndex, i);
            }
        }
    })
    return output;
};
console.log(twoSum([2,7,11,15], 9))
console.log(twoSum([3,2,4], 6))
console.log(twoSum([3,3], 6))
