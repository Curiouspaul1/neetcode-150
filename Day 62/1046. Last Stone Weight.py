

class Solution:
    def lastStoneWeight(self, stones) -> int:
        print(stones)
        if len(stones)<= 1:
            return len(stones)
    

        res = self.lastStoneWeight(self.reduceStoneArr(stones))
        return res

    def reduceStoneArr(self, arr):
        ar = sorted(arr, reverse=True)

        if (ar[0] == ar[1]):
            return ar[2::]
        else:
            res = abs(ar[0]-ar[1])
            arr = [res]
            arr.extend(ar[2::])
            
            return arr


l = Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])
print(l)
