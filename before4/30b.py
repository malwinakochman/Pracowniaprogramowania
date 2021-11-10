start = 0
N=int(input("Wprowadź liczbę liczb naturalnych: "))
count = int(0)
while count == N:
    for i in range(start, N+1):
        if i > 1:
            for j in range(2, i):
                if(i % j == 0):
            else:
                count +=1
                print(i)