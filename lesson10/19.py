class Statistics():
    def __init__(self):
        self.numbers = [12, 37, 6, 9, 17]
        self.max = 0
        self.min = 0
        self.mean = 0
        self.median = 0
    
    def add_number(self, number):
        self.numbers += [number]
        
    def display_numbers(self):
        print(*self.numbers)
    
    def determine_greatest(self):
        self.max = max(self.numbers)
    
    def determine_smallest(self):
        self.min = min(self.numbers)
    
    def calculate_mean(self):
        suma = 0
        for i in self.numbers:
            suma += i
        self.mean = suma/len(self.numbers)
        
    def calculate_median(self):
        sorted(self.numbers)
        if len(self.numbers) % 2 == 0:
            self.median = (self.numbers[len(self.numbers)//2] + self.numbers[len(self.numbers)//2 - 1]) / 2
        else:
            self.median = self.numbers[len(self.numbers)//2]
    
    def display_result(self):
        print(f"\nMinimum: {self.min}\nMaximum: {self.max}\nMean: {self.mean}\nMedian: {self.median}\n")
        

stat = Statistics()
stat.add_number(300)
stat.display_numbers()
stat.determine_greatest()
stat.determine_smallest()
stat.calculate_mean()
stat.calculate_median()
stat.display_result()


