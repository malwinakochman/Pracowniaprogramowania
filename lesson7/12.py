file = open('shopping.txt', 'a')
a= input('Podaj produkt: ')
file.write(a)
file.write('\n')
file.close()