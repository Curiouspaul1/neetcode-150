# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/914521126/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:

  
        final = [] 
        i = 0
        j = 0
        while i<len(nums1) and j<len(nums2):
            if nums1[i] <= nums2[j]:
                final.append(nums1[i])
                i += 1
            else:
                final.append(nums2[j])
                j += 1
        final = final + nums1[i:] + nums2[j:]
        size = len(final)
        return (final[size//2]) if size % 2 != 0 else (final[size//2 - 1] + final[(size//2)])/2 