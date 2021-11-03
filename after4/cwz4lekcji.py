#5
def display_university_address():
    print(2*"\nCracow University f Economics \nRakowicka 27 \n31-510 Kraków, POLAND")
    
display_university_address()

#6
def keyPhone():
    for i in range(1,10):
        print(i, end = " ")
        if i%3==0:
            print()

keyPhone()

#7
def multiplication(x, y):
    print(f"{x} * {y} = {x*y}")
    
multiplication(2, 5)

#8
def intigerNumbers(n):
    for i in range (1, n+1):
        print(i, end = " ")

intigerNumbers(15)

#9
def multiplication(x,y):
    return x*y

print( f"12 * 10 is {multiplication(12,10)}" )

#10
def read_number():
    x = int(input("Wprowadź liczbę: "))
    return x

number1 = read_number()
number2 = read_number()
sum1 = number1 + number2
print(f"Sum of those numbers is: {sum1}")

#15
import myma
x = myma.read_number()
y = myma.generate_number()

if x == y:
    print("You won!")
else:
    print("You lose :( ")
print(f"the number was: {y}")

#16

import mon

print(f"the name of the month 7 is {mon.month(7)}")

#17

def how_many_times():
    n = str(input("Enter letter: "))
    text = str(input("Enter text: ")) 
    
    count = 0
    for i in text:
        if i == n:
            count += 1
    
    return count
            
    
print(f"the letter e appears in the text {how_many_times()} times")

import howmany

print(f"the letter e appears in the text {howmany.how_many_times()} times")



