import 'dart:math' as math;
class Solution {
int lengthOfLongestSubstring(String s) {
    Set<String> substring = {};
    int maxLength = 0;
    int left = 0;
    int right = 0;
    while (right < s.length) {
        if (!substring.contains(s[right])) {
            substring.add(s[right]);
            maxLength = math.max(maxLength, substring.length);
            right++;
        } else {
            substring.remove(s[left]);
            left++;
        }
    }
    return maxLength;
}
}