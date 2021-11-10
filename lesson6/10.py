def sum1(array):
    sum2=0
    for i in array:
        sum2 += i
        
    return sum2

def array2str(array):
    together = " "
    for a in array:
        together+=str(a)
        together+=" "
    
    return together

array = [ 2, 3, 5 ]   
print("Array:", array2str(array))
print("Sum of values:", sum1(array))
