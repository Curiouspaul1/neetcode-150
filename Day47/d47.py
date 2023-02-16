# check the height of the left and right branches
# increment the value of l, r when the value on the left and right are not Null
# check the absolute difference between l and r,
# if the difference > 1 , return False, else return True.

def isBalanced(root):
    l, r = 0, 0

    if root is None:
        return True

    while root:
        right, left = root.right, root.left

        if right is not None:
            r += 1
        if left is not None:
            l += 1

    diff = abs(l-r)
    if diff > 1:
        return False
    return True
