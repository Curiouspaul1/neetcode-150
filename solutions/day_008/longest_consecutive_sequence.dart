import 'dart:math';

class Solution {
  int longestConsecutive(List<int> nums) {
    // create a set of the numbers
    Set<int> setNums = nums.toSet();
    // create a variable to store the max length
    int maxLength = 0;
    // loop through the set
    for (int x in setNums) {
      // if the number is not in the set, continue
      if (!setNums.contains(x - 1)) {
        // create a variable to store the length
        int length = 1;
        // create a variable to store the current number
        int current = x + 1;
        // loop through the set
        while (setNums.contains(current)) {
          // increment the length
          length++;
          // increment the current number
          current++;
        }
        // update the max length
        maxLength = max(maxLength, length);
      }
    }
    return maxLength;
  }
}
