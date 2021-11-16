def secondLargestElement():
    array2 = []
    x = max(array)
    for i in array:
        if i != x:
            array2 += [i]
    
    return max(array2)




array = [5,1,9,6,1]
print(secondLargestElement())