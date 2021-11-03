import random
def rand(fromm,to):
    x = random.randint(fromm,to)
    #while (x%2!=0 and x%3!=0) or (x%2!=0 and x%3==0) or (x%2==0 and x%3!=0):
    while not(x%2==0 and x%3==0):
        x = random.randint(fromm,to)
    return x
        
    

print(rand(10,50))
    