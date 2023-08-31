
import math

class Shape:
    def __init__(self, color, position):
        self.color = color
        self.position = position
    
    def calculatePerimeter(self):
        pass
    
    def calculateArea(self):
        pass

class Circle(Shape):
    def __init__(self, color, position, radius):
        super().__init__(color, position)
        self.radius = radius
    
    def calculatePerimeter(self):
        return 2 * math.pi * self.radius
    
    def calculateArea(self):
        return math.pi * self.radius ** 2
   
class Square(Shape):
    def __init__(self, color, position, side):
        super().__init__(color, position)
        self.side = side
    
    def calculatePerimeter(self):
       return 4 * self.side
    
    def calculateArea(self):
        return self.side **2
   
   
    
class Triangle(Shape):
    def __init__(self, color, position, base, height):
        super().__init__(color, position)
        self.base = base
        self.height = height
    
    def calculatePerimeter(self):
        return self.base + 2 * math.sqrt((self.base / 2) ** 2 + self.height ** 2)
    
    def calculateArea(self):
        return 0.5 * self.base * self.height

class Rectangle(Shape):
    def __init__(self, color, position, width, height):
        super().__init__(color, position)
        self.width = width
        self.height = height
    
    def calculatePerimeter(self):
        return 2 * (self.width + self.height)
    
    def calculateArea(self):
        return self.width * self.height

circle = Circle("red", { "x": 0, "y": 0 }, 5)
print("Perimeter of circle:", circle.calculatePerimeter())
print("Area of circle:", circle.calculateArea())
print("####################################")
triangle = Triangle("blue", { "x": 0, "y": 0 }, 4, 6)
print("Perimeter of triangle:", triangle.calculatePerimeter())
print("Area of triangle:", triangle.calculateArea())
print("####################################")
rectangle = Rectangle("green", { "x": 0, "y": 0 }, 3, 4)
print("Perimeter of rectangle:", rectangle.calculatePerimeter())
print("Area of rectangle:", rectangle.calculateArea())

print("####################################")
square = Square("red",{ "x": 0, "y": 0 },5)
print("Perimeter of square:", square.calculatePerimeter())
print("Area of Square:", square.calculateArea())
