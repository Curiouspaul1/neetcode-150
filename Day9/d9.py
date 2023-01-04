# remove the non-alphabet, whitespace and alphanumeric characters
# convert all uppercase to lowercase
# instantiate the left and right pointer to 0 and len(s) - 1
# while left <= right;
# check if s[left] = s[right]
# increment left and decrement right

import string
import re


def isPalindrome(s):
  formatedS = removeAlphanum(s)
  finalS = convertToLowercase(formatedS)
  l, r = 0, len(finalS) - 1
  print(formatedS, finalS)
  while l <= r:
    if finalS[l] == finalS[r]:
      continue
    else:
      return False
    l += 1
    r -= 1
  return True


def removeAlphanum(word):
  pattern = r'[' + string.punctuation + " " + ']'
  ans = re.sub(pattern, "", word)
  return ans


def convertToLowercase(word):
  return word.lower()

print(isPalindrome("A man, a plan, a canal: Panama"))
#print("hello")
# print(convertToLowercase("HelloWorld"))
# print(removeAlphanum("Hello@12*&fu)("))
