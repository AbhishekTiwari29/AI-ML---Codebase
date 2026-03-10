from abc import ABC , abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
        def __init__(self,radius):
            self.radius = radius

        def area(self):
            area = 3.14* self.radius*self.radius
            return area
        
class Rectangle(Shape):
        def __init__(self,length,width):
            self.length = length
            self.width = width

        def area(self):
            area = self.length*self.width
            return area 
        
class Triangle(Shape):
        def __init__(self,base,height):
            self.base = base
            self.height = height
        
        def area(self):
            area = 1/2*(self.base*self.height)
            return area 
        
c = Circle(5)
print(c.area())
r= Rectangle(5,10)
print(r.area())
t = Triangle(5,10)
print(t.area())