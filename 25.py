x="*"
a=int(input("Wprowadź a:"))
b=int(input("Wprowadź b:"))
print(x * b)
mid=a-2
for i in range(mid):
    print(x + " " * (b-2) + x)
print(x * b)