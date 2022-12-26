class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # check_set = set()

        # for n in nums:
        #     if n not in check_set:
        #         check_set.add(n)
        #     else:
        #         return True
        # return False

        return len(set(nums)) != len(nums)

