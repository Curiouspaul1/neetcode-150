function isPalindrome(s: string): boolean {
  s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
  if (s.split('').reverse().join('') === s) {
    return true;
  } else {
    return false;
  }
};

console.log(isPalindrome("A man, a plan, a canal: Panama"))
