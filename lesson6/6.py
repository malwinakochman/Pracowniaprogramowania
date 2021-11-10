numbers = [15, 8, 31, 47, 2, 19]
quantity = len(numbers)
sum1 = 0
for i in range(quantity):
    sum1 += numbers[i]
    
mean = sum1/quantity

print(mean)