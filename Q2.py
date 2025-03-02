
'''
Create a class named Book with instance variables title, author, ISBN, price, copies_available.
Implement methods:

__str__ to return book details.
borrow_book() to decrease available copies if a book is borrowed.
return_book() to increase available copies when a book is returned.
show_details() to display all book information.
From Book, inherit two classes:

Ebook with an additional instance variable file_size (in MB).
PrintedBook with an additional instance variable pages.
'''

class Book:
    def __init__(self, title, author, ISBN, price, copies_available):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.price = price
        self.copies_available = copies_available
    
    def __str__(self):
        return f"{self.title} by {self.author}, ISBN: {self.ISBN}, Price: ${self.price}, Available copies: {self.copies_available}"
    
    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            print("Book borrowed successfully.")
        else:
            print("Sorry, this book is out of stock.")
    
    def return_book(self):
        self.copies_available += 1
        print("Book returned successfully.")
    
    def show_details(self):
        print(self)

class Ebook(Book):
    def __init__(self, title, author, ISBN, price, copies_available, file_size):
        super().__init__(title, author, ISBN, price, copies_available)
        self.file_size = file_size
    
    def __str__(self):
        return super().__str__() + f", File Size: {self.file_size}MB"
    
    def show_details(self):
        print(self)

class PrintedBook(Book):
    def __init__(self, title, author, ISBN, price, copies_available, pages):
        super().__init__(title, author, ISBN, price, copies_available)
        self.pages = pages
    
    def __str__(self):
        return super().__str__() + f", Pages: {self.pages}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    ebook = Ebook("Digital Fortress", "Dan Brown", "1234567890", 9.99, 10, 5)
    printed_book = PrintedBook("Inferno", "Dan Brown", "0987654321", 14.99, 5, 480)
    
    ebook.show_details()
    printed_book.show_details()
    
    printed_book.borrow_book()
    printed_book.show_details()
    
    printed_book.return_book()
    printed_book.show_details()