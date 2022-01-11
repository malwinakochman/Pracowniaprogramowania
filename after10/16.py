class Ebook():
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page = 0
        self.status = False
    
    def open_ebook(self):
        self.status = True
        self.current_page = 1
        
    def close_ebook(self):
        self.status = False
    
    def next_page(self):
        if self.status == True:
            self.current_page += 1
        else:
            print("The book is close")
            
    def previous_page(self):
        if self.status == True:
            self.current_page -= 1
        else:
            print("The book is close")
    
    def show_status(self):
        if self.status == True:
            print(f"Title: {self.title}\nAuthor: {self.author}\nStatus: The ebook is open\nCurrent page: {self.current_page}")
        else:
            print(f"Title: {self.title}\nAuthor: {self.author}\nStatus: The ebook is close\nCurrent page: {self.current_page}")
    
            
            
ebook = Ebook("Harry Potter","J.K. Rowling","356")

ebook.show_status()
ebook.next_page()
ebook.open_ebook()
ebook.show_status()
ebook.next_page()
ebook.show_status()
        