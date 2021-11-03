def inrange(n,fromm,to):
    isInRange = False
    if n >= fromm and n <= to:
        isInRange = True
    
    return isInRange

print(inrange(3,2,5))