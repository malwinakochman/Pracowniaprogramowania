def rand_elem(array):
    import random
    x = random.choice(array)
    return x

array = [1, 2, 7, 8, 15, 16, 21, 22]
print(rand_elem(array))