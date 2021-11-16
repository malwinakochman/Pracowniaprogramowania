def reverseorder():
    reversearray = []
    x = len(array)
    for i in range(x-1, -1, -1):
        reversearray += [array[i]]
        
    return reversearray
    



array = [15, 8, 31, 47, 2, 19]
print(reverseorder())