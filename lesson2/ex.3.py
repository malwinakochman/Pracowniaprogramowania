squares = [1, 4, 9, 16, 25]

print(squares[0:3])
print(squares[:])
print(squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes) # replace the wrong value

cubes2 = [1, 2, 4, 8, 16]
cubes2.append(2 ** 5)
cubes2.append(2 ** 6)
print(cubes2)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
print(len(letters))