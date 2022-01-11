file = open("randomintegers.txt", "w")

import random

for i in range(1,51):
    x = random.randint(101,998)
    file.write(str(x))
    file.write("\n")
     
file.close()