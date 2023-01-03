def isConsecutive(nums): 
    numSet = set(nums)
    longest = 0
    for num in numSet:
        if num-1 not in numSet:
            currentNum = num
            currentStreak = 1
            while currentNum+1 in numSet:
                currentNum += 1
                currentStreak += 1
            longest = max(longest, currentStreak)
    return longest
    
a = [4, 2, 1, 6, 5]
b = [100,4,200,1,3,2]
print(isConsecutive(b))
print(isConsecutive(a))