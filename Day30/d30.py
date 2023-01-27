def searchArray(nums):
    left, right = 0, len(nums) - 1
    minimum = nums[0]
    
    while left <= right:
        if nums[left] < nums[right]:
            minimum = min(nums[left], minimum)
            break
        mid = (left + right) // 2 
        minimum = min(nums[mid], minimum)

        if nums[left] < nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return minimum
        

#nums = [3,4,5,1,2]
nums =[4,5,6,7,0,1,2]
print(searchArray(nums))