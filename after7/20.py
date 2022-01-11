file = open("numbers.txt","w")
for i in range(1,51):
    file.write(str(i))
    file.write("\n")
    
file.close()