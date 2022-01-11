array = [1,0,9,4,6]

def median(array):
    array.sort()
    
    if len(array) % 2 == 0:
        count = len(array)/2
        x = array[count]
        y = array[count+1]
        median = (x + y)/2
    else:
        count2 = len(array)-1
        x = array[count2] // 2


print(median(array))