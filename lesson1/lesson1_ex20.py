height=input("Enter your height in cm:")
weight=input("Enter your weight in kg:")
height=int(height)
weight=int(weight)
heightmeters=height/100
BMI=weight/(heightmeters)**2
print(f"BMI index:{BMI}")