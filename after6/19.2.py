def uniqueElements():
    unique = []
    for i in array:
        count = array.count(i)
        if count <= 1:
            unique += [i]
    
    return unique 
    
    
array = [2, 3, 2, 5, 8, 1, 9, 8]
print(uniqueElements())