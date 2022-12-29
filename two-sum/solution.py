class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort_nums=sorted(nums)
        print(sort_nums)
        l=0
        r=len(nums)-1
        while l<r:
            temp=sort_nums[l]+sort_nums[r]
            if temp < target:
                l=l+1
            if temp > target:
                r=r-1
            if temp == target:
                left=l
                right=r
                break
        i=0
        res=[]
        while i<len(nums):
            if sort_nums[left] == nums[i]:
                res.append(i)
                i=i+1
                continue
            if sort_nums[right] == nums[i]:
                res.append(i)
                i=i+1
                continue
            if len(res) == 2:
                break
            i=i+1
        return res

