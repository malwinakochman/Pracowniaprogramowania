amount = int(input("Enter the amount in PLN:"))
print(f"The amonut of PLN {amount} in coins:")

count = 0
for amount in range(1,amount+1):
    if amount % 5 == 0:
        count += 1
print(f"5 zł - {count}")

count2 = 0
rest1 = amount-count*5
for rest1 in range(1,rest1+1):
    if rest1 % 2 == 0:
        count2 += 1
print(f"2 zł - {count2}")

count3 = 0
rest2 = amount-count*5-count2*2
for rest2 in range(1,rest2+1):
        count3 += 1
print(f"1 zł - {count3}")