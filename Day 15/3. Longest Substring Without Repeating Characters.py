

# Solution link :https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/875719371/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        temp_str = ''

        for idx, i in enumerate(s):
            if i in temp_str:
                w= temp_str.index(i)
                w+=1
                print(w,i)
                temp_str = temp_str[w::] 
                temp_str+=i
                

                print(temp_str)


            else:
                temp_str +=i
            # if idx == len(s)-1:
            #     temp_str +=i
                print(temp_str)
            count = max(count, len(temp_str))
            

                
        return count