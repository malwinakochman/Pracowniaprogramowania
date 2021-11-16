array = [15, 2, 7, 16, 64, 2, 1, 0, 81, 28]
x = int(input("Enter value: "))
count = 0
for i in array:
    if i > x:
        count += 1

print(f"The number of elements that are greater than {x}: {count}")

