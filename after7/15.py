x = input("Enter the name of the file:")
file = open(x, "r")
count = 0
for line in file:
    count += 1

print(f"File name: {x} ")
print(f"Number of lines: {count}")