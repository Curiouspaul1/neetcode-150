function isAnagram(s: string, t: string): boolean {
    if (s.length !== t.length) return false;
    var len = s.length;
    var count = {};
    for (let i = 0; i < len; i++) {
        if (!count[s[i]]) count[s[i]] = 0;
        if (!count[t[i]]) count[t[i]] = 0;
        count[s[i]]++;
        count[t[i]]--;
    }
    for (let i in count){
        if (count[i] !== 0) return false;
    }
    return true;
};