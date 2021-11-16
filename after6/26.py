array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
odd = []
even = []
for i in array:
    if i % 2 == 0:
        even += [i]
    else:
        odd += [i]
sortarray = [*even]
sortarray += [*odd]
print(sortarray)