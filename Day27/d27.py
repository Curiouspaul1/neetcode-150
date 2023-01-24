# # crate a 
# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         l, r = 0, len(nums) - 1

#         while l <= r:
#             m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
#             if nums[m] > target:
#                 r = m - 1
#             elif nums[m] < target:
#                 l = m + 1
#             else:
#                 return m
#         return -1

def binarySearch(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
        if nums[m] > target:
            r = m - 1
        elif nums[m] < target:
            l = m + 1
        else:
            return m
    return -1

nums = [1,0,3,5,9,12]
target = 2
print(binarySearch(nums, target))
#print((12//5))


