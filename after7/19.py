file = open("shoppinglist.txt","w")
list1 = open("MeatAndFish.txt","r")
list2 = open("GrainsAndBread.txt","r")

file.write(list1.read())
file.write(list2.read())


file.close()
list1.close()
list2.close()