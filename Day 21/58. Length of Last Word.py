class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        
        
        count = 0


        for i in range(len(s)):


            if s[i].isalpha():

                count +=1 

                length = count 


            else:


                count = 0 

        return length 