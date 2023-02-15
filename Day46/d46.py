def diameterOfTree(root):
    left, right = 0,0
    curVal = root


    while curVal is not None:
        if curVal.left  is not None:
            left += 1
            curVal = curVal.left
        elif curVal.right is not None:
            right += 1
            curVal = curVal.right


    maxDiameter = left + right
    
    maxDiameter = max(maxDiameter, left + right)
    return maxDiameter
