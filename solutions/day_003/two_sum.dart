class Solution {
  List<int> twoSum(List<int> nums, int target) {
    //get the length of the array
    int numsLength = nums.length;

    for (int i = 0; i < numsLength - 1; i++) {
      //loop through the array and check if the sum of the current element and the next element is equal to the target
      for (int j = i + 1; j < numsLength; j++) {
        if (nums[i] + nums[j] == target) {
          return [i, j];
        }
      }
    }

    return [];
  }
}
