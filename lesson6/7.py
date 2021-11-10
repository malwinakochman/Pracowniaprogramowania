numbers = [ 2, 5, 7, 6, 15]
even = 0
odd = 0
quantity = len(numbers)
for i in numbers:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1
        
print(even)
print(odd)



