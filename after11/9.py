class Book():
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
        
class paperBook(Book):
    def __init__(self, title, author, year, numberOfPages):
        self.numberOfPages = numberOfPages
        super().__init__(title,author,year)
    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nNumber of pages: {self.numberOfPages}"
    
class eBook(Book):
    def __init__(self, title, author, year, nameOfFile):
        self.nameOfFile = nameOfFile
        super().__init__(title,author,year)
    def __str__(self):
        return f"\nTitle: {self.title}\nAuthor: {self.author}\nYear: {self.year}\nName of file: {self.nameOfFile}"


paperBook = paperBook("Wiedźmin","Andrzej Sapkowski", 1986, 360)
print(paperBook)
eBook = eBook("Tamte dni, tamte noce","Aciman Andre", 2007, "tamtednitamtenoce.pdf")
print(eBook)