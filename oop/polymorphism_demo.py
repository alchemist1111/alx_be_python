import math

# Parent class
class Shape:
    def area(self):
        """Parent class method that raises NotImplementedError."""
        raise NotImplementedError("Subclasses must implement this method")




class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        """Constructor for Rectangle."""
        self.length = length
        self.width = width
        
    def area(self):
        """Overrides the area method to calculate the area of a rectangle."""
        return self.length * self.width    



class Circle(Shape):
    def __init__(self, radius: float):
        """Constructor for Circle."""
        self.radius = radius
        
    def area(self):
        """Override the area method to calculate the area of a circle."""
        return math.pi * self.radius ** 2    