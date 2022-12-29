var groupAnagrams = function(strs) {
    // this is the final array that will be returned
    let anagrams = [];
    // I'll use this object to map out the anagrams
    let curr = {};
    /*
    * this loops through the array of strings
    * splits the word and sort it alphabetically, it then joins it back together
    * (doing this will make sure that the words that are anagrams will have the same arrangement of letters)
    */
    for (let str of strs) {
        let key = str.split('').sort().join('');
        /*
        * I then loop though the object I created earlier and check if it has a property with the name of the key.
        * if it does, I push the current string into the array that is the value of the property
        * if it doesn't, I create a new property with the key as the name and the value as an array with the current string
        */
        if(key in curr) {
            curr[key].push(str);
        } else {
            curr[key] = [str];
        }
    }
    /*
    * I then loop through the "curr" object with its keys and push the values into the "anagrams" array
    */
    for (const key of Object.keys(curr)) {
        anagrams.push(curr[key]);
    }
    return anagrams;
};
console.log(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]));
console.log(groupAnagrams([""]));
console.log(groupAnagrams(["a"]));
