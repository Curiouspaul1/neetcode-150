import 'dart:collection';

class Solution {
  List<List<String>> groupAnagrams(List<String> strs) {
    // create a map to store the sorted string as the key and the list of strings as the value
    // HashMap is used because it is faster than the Map class
    HashMap<String, List<String>> map = HashMap();
    for (String str in strs) {
      // split the string into a list of characters
      List<String> chars = str.split("");
      // sort the list of characters
      chars.sort();

      String sortedStr = chars.toString();
      // if the map does not contain the sorted string, add it to the map with an empty list as the value
      map.putIfAbsent(sortedStr, () => []);
      // add the string to the list of strings
      map[sortedStr]?.add(str);
    }

    return map.values.toList();
  










  }
}