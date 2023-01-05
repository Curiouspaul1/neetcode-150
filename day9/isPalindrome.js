/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
  let letters ="abcdefghijklmnopqrstuvwxyz0123456789";
  let test = s.toLowerCase().split("").filter(a => letters.includes(a)).join("");
  let rev = test.split("").reverse().join("");
  return test === rev;
};
