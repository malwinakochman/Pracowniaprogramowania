class Ebook():
    
    def __init__(self):
        self.title = "Ania z zielonego wzgórza"
        self.author = "Lucy Maud Montgomery"
        self.pages = 352
        self.current_page = 1
        self.open = False
    
    def display_status(self):
        print(f"\nTitle: {self.title},\nAuthor: {self.author},\nPage numbers: {self.pages},\nCurrent page number: {self.current_page}\n")
    
    def open_book(self):
        self.open = True
        print("Book is open")
        
    def close(self):
        self.open = False
        print("Book is close")
        
    def read(self):
        if self.open == True:
            print("Book is open, you can read")
        else:
            print("Book is close, you can't read")
            
    def next_page(self):
        if self.open == True:
            self.current_page += 1
        else:
            print("Book is close, you can't go to the next page")
        
    def previous_page(self):
        if self.open == True:
            self.current_page -= 1
        else:
            print("Book is close, you can't go to previous page")
    
        
            
ebook = Ebook()
ebook.open_book()
ebook.display_status()
ebook.next_page()
ebook.next_page()
ebook.next_page()
ebook.next_page()
ebook.next_page()
ebook.display_status()
ebook.close()
ebook.next_page()
ebook.next_page()
ebook.next_page()
