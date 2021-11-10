number = int(input("Enter number: "))
quantity = int(0)
suma = int(0)
mean = int(0)
while number != 0:
    quantity += 1
    suma += number
    mean = suma/quantity
    number = int(input("Enter number: "))
print(f"RESULT: Quantity={quantity}, Sum={suma}, Mean={mean}")
    
    
    
    