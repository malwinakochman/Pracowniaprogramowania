class Thermometer():
    
    def __init__(self):
        self.temperature = 0
        self.is_on = False
   
    def show_status(self):
        if self.is_on == True:
            if self.temperature >= 37 and self.temperature < 41:
                print(f"Temperature: {self.temperature}C (fever)")
            elif self.temperature >= 41:
                print(f"Temperature: {self.temperature}C (CRITICAL TEMPERATURE!!)")
            else:
                print(f"Temperature: {self.temperature}C")
        else:
            print("Thermometer is off!")

    def turn_on(self):
        self.is_on = True
    
    def turn_off(self):
        self.is_on = False
    
    def measure_temperature(self):
        import random
        self.temperature = round(random.uniform(34.0,42.0), 1)
        

temp = Thermometer()
temp.turn_on()
temp.measure_temperature()
temp.show_status()