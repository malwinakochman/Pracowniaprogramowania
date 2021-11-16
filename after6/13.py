def powersofnumbers():
    x = 0
    array2 = []
    for i in range(len(array)):
        x += 1
        array2 += [array[i]**2]
    return array2
            
    

array = [8, 2, 5, 1, 9]
print(f"Array: {array}")
print(f"2nd power: {powersofnumbers()}")

