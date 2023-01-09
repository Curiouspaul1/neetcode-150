class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        countGap={0:0}
        for r in wall:
            total=0
            for i in r[:-1]:
                total=total+i
                countGap[total]= 1+countGap.get(total,0)
        return len(wall)-max(countGap.values())
