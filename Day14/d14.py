def bestTime(nums):
    l,r = 0,1
    profit = 0

    while l < len(nums):
        if nums[r] < nums[l]:
            l = r
        if nums[r] - nums[l] > profit:
            profit = nums[r] - nums[l]
        r += 1
    return profit

p = [7,6,4,3,1]
print(bestTime(p))