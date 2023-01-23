# create two pointers, l, r = 0,1
# while r < len(arr)
# calculate the area of using, (l-r)(min(arr[l], arr[r]))

# return the area


def maxArea(heights):
    l,r = 0,1
    area = 0
    while r < len(heights):
        curArea = (r-l + 1) * (min(heights[l], heights[r]))
        if curArea < area:
            r += 1
        else:
            area = max(area, curArea)
        

    
    return area


heights = [2,1,5,6,2,3]

print(maxArea(heights))
