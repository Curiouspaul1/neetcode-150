class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str

        :rtype: bool
        """
        s_new=""
        char_set=set("abcdefghijklmnopqrstuvwxyz1234567890")
        for i in s:
            i=i.lower()
            if i in char_set:
                s_new=s_new+i
        r,l = 0, len(s_new)-1
        while r<l:
            
            if s_new[r] != s_new[l]:
                return False
            r=r+1
            l=l-1
        return True

        # temp=""
        # for i in range(len(s_new)-1,-1,-1):
        #     temp=temp+s_new[i]
        # return s_new==temp

