import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}", message)
suma = 0
count = 0
for i in temperatures:
    suma += int(i)
    count += 1
    
print(suma/count)