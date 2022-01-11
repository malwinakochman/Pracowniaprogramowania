import re
text = "To be, or not to be, that is the question"
words = re.split("\s", text)
for i in words:
    if len(i) >= 6:
    