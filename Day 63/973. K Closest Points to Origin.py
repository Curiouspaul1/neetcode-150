

class Solution:
    def kClosest(self, points, k: int) :
        my_dict = []
      # Calulating Distance using Distance Fromula
        for i in points:
            y = (i[0]**2+i[1]**2)**0.5
            y = [i,y]
            my_dict.append(y)
        # Sorting the values on the basis of their distance from Orign in ascending order
        my_dict.sort(key = lambda x:x[1])
        x = my_dict[0][1]
        j = 0
        z = []
        # Getting K closest point from Orign
        while j<k:
            z.append(my_dict[j][0])
            j+=1
        return z



    
    

        

print(Solution().kClosest([[1,3],[-2,2], [2,-2]], 2))
