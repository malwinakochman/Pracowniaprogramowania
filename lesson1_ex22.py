import random
result=random.randint(1,6)
answer=input("Guess the number:")
answer=int(answer)
if answer==result:
    print("True")