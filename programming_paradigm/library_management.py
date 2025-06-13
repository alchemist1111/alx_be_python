class Book:
    def __init__(self, title, author):
        """
        Initialize a Book instance with title and author.
        _is_checked_out tracks availability (private attribute).
        """
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def check_out(self):
        """
        Mark the book as checked out.
        """
        self._is_checked_out = True
        
    def return_book(self):
        """
        Mark the book as available (not checked out).
        """
        self._is_checked_out = False
        
    def is_available(self):
        """
        Return True if the book is not checked out.
        """
        return not self._is_checked_out
    
    
class Library:
    def __init__(self):
        """
        Initialize the library with an empty list of books (private attribute).
        """
        self._books = []
        
    def add_book(self, book):
        """
        Add a Book instance to the library's collection.
        """
        self._books.append(book)
        
    def check_out_book(self, title):
        """
        Check out a book by title. If found and available, mark as checked out.
        """
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"Sorry, '{title}' is not available for checkout.")
        
    def return_book(self, title):
        """
        Return a book by title. If found and checked out, mark as returned.
        """
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out or does not exist in the library.")
        
    def list_available_books(self):
        """
        Print all books that are currently available.
        """
        available = [book for book in self._books if book.is_available()]
        if not available:
            print("No books are currently available.")
        else:
            for book in available:
                print(f"{book.title} by {book.author}")                                