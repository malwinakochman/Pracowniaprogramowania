class Phone():
    def __init__(self, brand, model, year):
        self.turn_on = False
        self.brand = brand
        self.model = model
        self.year = year
    
    def TurnOn(self):
        self.turn_on = True
    
    def TurnOff(self):
        self.turn_on = False
    
    def __str__(self):
        return f"Brand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nTurned on: {'Yes' if self.turn_on ==  True else 'No'}"


phone = Phone("Samsung", "Note 10", 2019)
phone.TurnOn()
print(phone)
phone2 = Phone("Apple", "13 pro", 2021)
phone2.TurnOn()
print(phone2)
phone2.TurnOff()
print(phone2)

