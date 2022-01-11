class Students():
    def __init__(self, name, surname, ID, field):
        self.name = name
        self.surname = surname
        self.id = 100000
        self.field = field
        
    def __str__(self):
        return f"\nName: {self.name}\nSurname: {self.surname}\nID: {self.id}\nField: {self.field}"
    

students = Students("Malwina", "Kochman", "000000", "Informatyka Stosowana")
print(students)