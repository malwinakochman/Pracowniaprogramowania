def whichNameIsTheLongest():
    lenh = []
    for i in range(len(names)):
        lenh += [len(names[i])]
    x = max(lenh)
    for b in range(len(lenh)):
        if lenh[b] == x:
            y = names[b]
        
    return y
    

names = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
print(whichNameIsTheLongest())    