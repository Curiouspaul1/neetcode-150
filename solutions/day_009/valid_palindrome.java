import java.util.regex.Matcher;
import java.util.regex.Pattern;

class Solution {
  public boolean isPalindrome(String s) {
    // 1. Remove all non-alphanumeric characters
    Pattern pattern = Pattern.compile("[^a-z0-9]");
    // 2. Convert to lower case
    Matcher matcher = pattern.matcher(s.toLowerCase());
    // 3. Remove all non-alphanumeric characters
    String processedString = matcher.replaceAll("");
    // 4. Check if the string is a palindrome
    return processedString.equals(new StringBuilder(processedString).reverse().toString());
  }
}