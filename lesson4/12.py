def suma(N):
    sum1 = 0
    N = int(N)
    for i in range(1,N+1):
        sum1 += i
    
    return sum1

print(suma(10))