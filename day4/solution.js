var groupAnagrams = function (strs) {
  let result = {}
  for (let word of strs) {
    let sortedWord = word.split('').sort().join('')
    if (result[sortedWord]) {
      result[sortedWord].push(word)
    } else {
      result[sortedWord] = [word]
    }
  }
  return Object.values(result)
}

groupAnagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat'])
