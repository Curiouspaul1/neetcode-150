function containsDuplicate(nums: number[]): boolean {
    const newMap = {};
    for (let i of nums) {
        if (newMap[i]) return true;
        newMap[i] = true;
    }
    return false;
};