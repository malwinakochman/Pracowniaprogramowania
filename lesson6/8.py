numbers = [ -15, 8, -21, 47, -2, 19 ]
mx = numbers[0]
mn = numbers[0]
for i in range(len(numbers)):
    if numbers[i]>mx:
        mx=numbers[i]
    if numbers[i]<mn:
        mn=numbers[i]
print(f"Najmniejsza liczba: {mn}")
print(f"Największa liczba: {mx}")