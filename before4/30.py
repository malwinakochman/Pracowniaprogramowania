N=int(input("Wprowadź liczbę liczb naturalnych: "))
for a in range(1,N+1):
    if a>1:
        for b in range(1, a+1):
            if (a % b == 0):
                break
            else:
                print(a)