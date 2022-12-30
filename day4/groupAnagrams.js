/**
 * @param {string[]} strs
 * @return {string[][]}
 */    
var groupAnagrams = function(strs) {
	let lookUp = {};
  let result = [];
  for (let i = 0; i < strs.length; i++) {
    let key = strs[i].split("").sort();
    if (!lookUp[key]) lookUp[key] = [strs[i]];
    else lookUp[key].push(strs[i]); 
  }
  for (let key of lookUp) {
    result.push(lookUp[key]);
  }
  return result;
}
