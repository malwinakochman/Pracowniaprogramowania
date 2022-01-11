import re

text = "To be, or not to be, that is the question"
vowels = re.findall("[aeiou]", text)
count = 0
for i in vowels:
    count += 1
    
print(count)