def coins(price):
    count=0
    while price//5>0:
        count+=price//5
        price=price%5
    while price//2>0:
        count+=price//2
        price=price%2
    while price//1>0: 
        count+=price//1
        price=price%1
        
    return count
    
print(coins(7))