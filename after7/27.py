import re
text = open("text16.txt", "r")
text_content = text.read()
words = re.split("\s", text_content)
for i in words:
    x = len(i)
    if x >= 6 and i[x-1] != "." and i[x-1] != "," and i[x-1] != " ":
        print(i)
                