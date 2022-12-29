# Solution Link https://leetcode.com/problems/group-anagrams/submissions/867584244/

class Solution:
    def groupAnagrams(self, strs):
        mapResult = {}
        
        if len(strs) == 0 :
            return [['']]
        
        for i in strs:
            res =str(''.join(sorted(i)))
            if res in mapResult:
                mapResult[res].append(str(i))
            else:
                mapResult[res] = [str(i)]

        return list(mapResult.values())



Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])