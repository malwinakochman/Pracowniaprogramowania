def bonus(years):
    bonuss=0
    for i in range(1,years+1):
        if i<=5:
            bonuss+=100
        elif i>=6 and i<=8:
            bonuss+=200
        else:
            bonuss+=50
    return bonuss

print(bonus(9))


        
        