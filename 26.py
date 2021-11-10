pin = int(5578)
for i in range(1,4):
    test = int(input("Enter the PIN code: "))
    if test == pin:
         print("Correct")
         break
    else:
        if i!=3:
            print("Incorrect")
        else:
            print("Sorry, your payment card has been blocked.")
        
