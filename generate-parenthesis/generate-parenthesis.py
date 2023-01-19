class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = [('', 0)]
        for i in range(n*2):
            sub_res = []
            for seq, num in res:
                if num < n:
                    sub_res.append((seq + '(', num + 1))
                if num > len(seq)/2:
                    sub_res.append((seq + ')', num))
            res = sub_res
        return [r[0] for r in res]