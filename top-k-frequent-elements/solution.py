class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        temp=defaultdict(int)
        freq=[[] for i in range(len(nums)+1)]
        for i in nums:
            temp[i]=temp[i]+1
        for n,c in temp.items():
            freq[c].append(n)
        res=[]
        for i in range(len(nums), -1, -1):
            for c in freq[i]:
                res.append(c)
            if len(res)==k:
                return res 


        