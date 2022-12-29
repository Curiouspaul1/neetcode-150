function groupAnagrams(strs: string[]): string[][] {
    let obj = {};
    for (let words of strs){
        let letters = words.split("").sort().join("");
        obj[letters] ? obj[letters].push(words) : obj[letters] = [words];
    }
    return Object.values(obj);
};