class Solution {
List<List<int>> threeSum(List<int> nums) {
  // Sort the array
  nums.sort();
  // Create a list to store the result
  var res = <List<int>>[];
  // Iterate through the array
  for (var i = 0; i < nums.length; i++) {
    if (i > 0 && nums[i] == nums[i-1]) {
      // Skip the duplicate
      continue;
    }
    var l = i + 1;
    // The right pointer starts from the end of the array
    var r = nums.length - 1;
    // Iterate through the array
    while (l < r) {
      // Calculate the sum
      var s = nums[i] + nums[l] + nums[r];
      // If the sum is less than 0, move the left pointer to the right
      if (s < 0) {
        // Skip the duplicate
        l++;
      // If the sum is greater than 0, move the right pointer to the left
      } else if (s > 0) {
        r--;
      } else {
        // If the sum is 0, add the result to the list
        res.add([nums[i], nums[l], nums[r]]);
        while (l < r && nums[l] == nums[l+1]) {
          l++;
        }
        while (l < r && nums[r] == nums[r-1]) {
          r--;
        }
        // Move the left and right pointers
        l++;
        // Move the right pointer to the left
        r--;
      }
    }
  }
  return res;
}

}