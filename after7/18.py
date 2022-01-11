file = open("copylines.txt", "w")
fileToCopy = open("text16.txt", "r")
for line in fileToCopy:
    file.write(line)
file.close()
fileToCopy.close()