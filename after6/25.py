def minmax(array):
    x = min(array)
    y = max(array)
    array2 = [x]
    array2 += [y]
    
    return array2

array = [4,2,8,4,7,9,5]
print(minmax(array))