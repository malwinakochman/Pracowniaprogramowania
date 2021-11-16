def occurs(number, array):
    for i in array:
        if number == i:
            return True

array = [15, 38, 7, 23, 14]
number = int(input("Enter the number: "))
print(f"Number: {number}")
print(f"Array: {array}")
if occurs(number, array) == True:
    print(f"Result: number {number} appears in the array")
else:
    print(f"Result: number {number} don't appears in the array")


