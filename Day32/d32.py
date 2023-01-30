def median(m, n):
    # merge the two sorted arrays
    mergedArray =  m + n
    mergedArray.sort()
    print(mergedArray)


    if len(mergedArray) % 2 == 1:
        mid = len(mergedArray) // 2
        return mergedArray[mid]
    else:
        mid = len(mergedArray) // 2
        return (mergedArray[mid] + mergedArray[mid - 1] ) /2
    

    # if len(mergedArray) % 2 == 0
    # mid = len(mergedArray) // 2
    # return (mergedArray[mid] + mergedArray[mid + 1] ) / 2
    # else: 
    # mid = len(mergedArray) // 2
    # return mergedArray[mid] 
    

m, n = [1,2], [3, 4]
print(median(m, n))