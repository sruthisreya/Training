from abc import ABC
class Shape(ABC):
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius*self.radius
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length*self.width
    
circle=Circle(radius=9)
print("area of circle is" ,circle.area())
rectang=Rectangle(length=23,width=33)
print("area of rectangle is",rectang.area())