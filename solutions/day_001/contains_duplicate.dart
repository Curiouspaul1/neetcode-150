class Solution {
  bool containsDuplicate(List<int> nums) {
    Set<int> checkedVar = Set();

    for (int num in nums) {
      //"!" very important, if you don't use it, it will return false even if there is a duplicate
      if (!checkedVar.contains(num)) {
        checkedVar.add(num);
      } else
        return true;
    }
    return false;
  }
}
