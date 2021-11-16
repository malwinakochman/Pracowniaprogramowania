def median(array):
    array.sort()
    if len(array) % 2 == 0:
        index2 = len(array) // 2
        x = (array[index2] + array[index2-1]) / 2
    else:
        index1 = len(array) // 2
        x = array[index1]
        
    return x

#a
array = [1,0,9,4,6]
print(median(array))

#b
array = [6, 8, 3, 1, 0, 4, 7]
print(median(array))