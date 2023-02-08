def findDuplicate(nums):
    values = set()

    for val in nums:
        if val not in values:
            values.add(val)
        else:
            return val
