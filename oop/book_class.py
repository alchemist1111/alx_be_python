# Book class
class Book:
    # Constructor
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year
        
        
    def __del__(self):
        """Destructor to print a message when the book object is deleted."""
        print(f"Deleting {self.title}")
        
    def __str__(self):
        """String representation for the book instance."""
        return f"{self.title} by {self.author}, published in {self.year}"
    
    def __repr__(self):
        """Official representation for the book instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"        