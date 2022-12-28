class Solution {
  bool isAnagram(String s, String t) {
    if (s.length != t.length) {
      return false;
    }
// double dot operator is used to chain methods together
// double dot is used for the sort method so as not to return a new list or void error
    List<String> sList = s.split('')..sort();
    List<String> tList = t.split('')..sort();

    for (var i = 0; i < sList.length; i++) {
      if (sList[i] != tList[i]) {
        return false;
      }
    }
    return true;
  }
}
