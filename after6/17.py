def firstdonotappearsecond():
    newArray = []
    count = 0
    for i in array1:
        for a in array2:
            if count < len(array2):
                if i == a: 
                    count += 0
                    break
                else:
                    count += 1
                    if count == 3:
                        newArray += [i]
            else:
                count = 0
                if i == a: 
                    count += 0
                    break
                else:
                    count += 1
                    if count == 3:
                        newArray += [i]
    return newArray

    
array1 = [4, 36, 12, 28, 9, 44, 5]
array2 = [5,1,36]
print(firstdonotappearsecond())

