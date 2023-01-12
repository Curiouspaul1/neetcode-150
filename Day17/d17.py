#def checkInclusion(s1,s2):
    # save all the permutation of s1 in a set called s1Set
    # use sliding window to check if s2 contain any element of s1Set
    # if yes return true, else return False

import itertools
a = "abcd"
x = " ".join(a)

def setConverter(a):
    b =[p for p in itertools.permutations(a)]
    ans = []
    for i in b:
        c = "".join(i)
        ans.append(c)
    return set(ans)

def stringPermutation(s1,s2):
    s1Set = setConverter(s1)
    for i in s1Set:
        if i in s2:
            return True
    
    return False

s1 = "ab"
s2 = "eidboaoo"
print(stringPermutation(s1, s2))

