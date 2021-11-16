array1 = [1,0,3,5,12]
array2 = [1,7,3,2,3,4,0,5,7,12]
count = 0
for i in array1:
    for x in array2:
        if i == x:
            count += 1
            break
if count == len(array1):
    print("The first array is a subset of the second one")
else:
    print("The first array isn't a subset of the second one")