class Solution(object):
    def topKFrequent(self, nums, k):
        nums_map = dict()

        for i in range(len(nums)):
            num = nums[i]
            if nums_map.get(num) != None:
                nums_map[num] = nums_map.get(num) + 1
            else:
                nums_map[num] = 1

        ans = []

        for i in range(k):
            ans.append(max(nums_map, key=nums_map.get))
            nums_map.pop(ans[-1])

        return ans
