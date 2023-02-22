def traverseTree(root):
    current = root
    allItems = []
    allItems.append(list(current))


    while current.left or current.right:
        newValRight, newValLeft = current.right.val, current.left.val

        if newValRight or newValLeft is None:
            pass
        allItems.append(list(newValRight, newValRight))

    return allItems


