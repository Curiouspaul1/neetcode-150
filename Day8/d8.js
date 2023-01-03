const isConsecutive = (nums) => {
    // create a set from the array
    const set = new Set(nums);
    var longestStreak = 0;
    for (let i in nums) {
        if ( !set.has(i - 1)) {
            var currentNum = i;
            var currentStreak = 1;
            while (set.has(currentNum + 1)) {
                currentNum++;
                currentStreak++;
            }
            longestStreak = Math.max(longestStreak, currentStreak);
        }
        return longestStreak;
    }
}

var nums = [100, 4, 200, 1, 3, 2];
console.log(isConsecutive(nums));