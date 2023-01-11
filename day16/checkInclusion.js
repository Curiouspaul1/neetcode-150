/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
  let map = {};
  let clone = {};
  for (let i = 0; i < s1.length; i++) {
    if (!map[s1[i]]) {
      map[s1[i]] = 0;
      clone[s1[i]] = 0;
    };
    map[s1[i]]++;
    clone[s1[i]]++;
  }
  let x = 0;
  let count = 0;
  let p = 0;
  while (x < s2.length) {
    let sub = s2.substr(x, s1.length);
    while (p < sub.length) {
      if (map[sub[p]] > 0) {
        map[sub[p]]--;
        count++
      } else {
        count = 0;
        p = 0;
        map = {...clone};
        break;
      };
      if (count === s1.length) return true;
      p++;
    }
    x++;
  }
  return false;
};
