

# https://leetcode.com/problems/time-based-key-value-store/submissions/914385028/
class TimeMap:

	def __init__(self):

		self.dict = {}

	def set(self, key: str, value: str, timestamp: int) -> None:

		if key not in self.dict:
			self.dict[key] = {}

		self.dict[key][timestamp] = value

	def get(self, key: str, timestamp: int) -> str:

		if key not in self.dict:
			return ''

		while timestamp > 0:

			if timestamp in self.dict[key]:
				return self.dict[key][timestamp]

			timestamp = timestamp - 1

		return ''
	


    # Alternative solution without Tle:

    # How to know when to use binary search -> Constraints
# O(logN)
class TimeMap:
  # bin search soln
  def __init__(self):
    self.store = {} # hashmap, key = string, val = [list of [val, timestamp]] {foo -> [bar, 1]}

  def set(self, key: str, value: str, timestamp: int) -> None:
    if key not in self.store:
      # insert
      self.store[key] = [] # set to empty list.
    self.store[key].append([value, timestamp]) # append val & times

  def get(self, key: str, timestamp: int) -> str:
    res = "" # if not exist just return empty
    values = self.store.get(key, []) # find match it'll return that list if doesn't then returns empty list (by default) [values is a list]
    
    # binary  search
    low, high = 0, len(values) - 1
    while low <= high:
      mid = (low + high) // 2
      # values[mid] will be a pair of values and timestamps
      # we only need to check timestamps (which is in incr order) hence values[mid][1]
      if values[mid][1] <= timestamp:
        # if equal or less than timestamp -> ans found
        res = values[mid][0] # closest we've seen so far -> store in ans
        low = mid + 1 # check for closer values
      else:
        # not allowed (acc to question)
        high = mid - 1 # don't assign any result here as this is an invalid val
    return res