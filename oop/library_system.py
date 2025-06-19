# Book class
class Book:
    """Parent class constructor for book attributes"""
    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author
        
        
    def __str__(self):
        """String representation for the base class"""
        return f"Book: {self.title} by {self.author}"    

# Book subclasses
class EBook(Book):
    def __init__(self, title:str, author:str, file_size:int):
        """Constructor for the EBook class, inheriting from Book and adding file_size."""
        super().__init__(title, author) # Call the parent constructor
        self.file_size = file_size
        
    def __str__(self):
        """String representation for the EBook class."""
        return f"EBook: {self.title} by {self.author}, File size: {self.file_size}KB"    


class PrintBook(Book):
    def __init__(self, title:str, author:str, page_count:int):
        """Constructor for the PrintBook class, inheriting from Book and adding page_count."""
        super().__init__(title, author) # Call the parent constructor
        self.page_count = page_count
        
    def __str__(self):
        """String representation for the PrintBook class."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Library class to manage a collection of books."""
        self.books = []
        
    def add_book(self, book: Book):
        """Add a book or ebook/printbook to the library."""
        self.books.append(book)
        
    def list_books(self):
        """List all books in the library with their details."""
        for book in self.books:
            print(book)        