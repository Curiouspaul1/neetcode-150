# Solution Link:  https://leetcode.com/problems/koko-eating-bananas/submissions/881596060/
import math



class Solution:
    def minEatingSpeed(self, piles, h: int) :
        l,r =1, max(piles)
        ans = r
        
        def checkthrough(mid):
            hr = 0
            for i in piles:
                hr += math.ceil(i/mid)
            
            return hr
        
        while l<=r :
            mid = (l+r)//2
            if checkthrough(mid) <= h:
                ans =min( mid, ans)
                r = mid-1
            else:
                l =mid+1
            
        return ans