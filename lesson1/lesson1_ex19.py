a=input("Wprowadź bok trójkąta a:")
b=input("Wprowadź bok trójkąta b:")
c=input("Wprowadź bok trójkąta c:")
a=int(a)
b=int(b)
c=int(c)

p=(1/2)*(a+b+c)
area=(p*(p-a)*(p-b)*(p-c))**(1/2)
area=int(area)
print(area)