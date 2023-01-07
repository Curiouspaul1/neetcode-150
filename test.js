function isPalindrome(s) {
    s = s.replace(/[^a-zA-Z0-9]/g, '').toLowerCase();
    console.log('With join', s.split('').reverse().join(''));
    console.log('Without join', s.split('').reverse().join());
    if (s.split('').reverse().join('') === s) {
        return true;
    }
    else {
        return false;
    }
}
;
console.log(isPalindrome("A man, a plan, a canal: Panama"));
