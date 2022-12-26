var containsDuplicate = function (nums) {
  let frequency = {}
  for (let val of nums) {
    frequency[val] = (frequency[val] || 0) + 1
    if (frequency[val] > 1) {
      return true
    }
  }
  return false
}
