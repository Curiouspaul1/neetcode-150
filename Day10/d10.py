def twoSum(numbers, target):
    l, r = 0, len(numbers) - 1
    while l < r:
            sum = numbers[l] + numbers[r] 
            if sum > target:
                r -= 1
            elif sum < target:
                l += 1
            else:
                return [l+1, r+1]


a, t = [-1,0], -1
print(twoSum(a, t))