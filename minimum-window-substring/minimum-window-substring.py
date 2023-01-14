class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if len(t) == 0:
            return ""
        
        counT = {}
        window = {}
        
        l = 0
        
        res, res_len = [-1, -1], float('inf')
        
        
        for c in range(len(t)):
            counT[t[c]] = 1 + counT.get(t[c], 0)
            
        have, need  = 0, len(counT)
        
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            
            if c in counT and window[c] == counT[c]:
                have = have + 1
                
            while have == need:
                if( r - l + 1) < res_len :
                    res_len = (r - l + 1)
                    res= [l, r]
                    
                
                window[s[l]] -=1
                
                if s[l] in counT and window[s[l]] < counT[s[l]]:
                    have -=1
                    
                l = l + 1
                
                
        l, r = res
                
        return s[l:r+1] if res_len != float('inf') else ""                
            
            
            
            
        