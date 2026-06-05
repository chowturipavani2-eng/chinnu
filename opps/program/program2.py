
class Circle:
    pi = 3.14159

    def __init__(self, radius):
        self.radius = radius
    def area(self):            
        return Circle.pi * self.radius * self.radius

    @classmethod
    def unit_circle(cls):     
        return cls(1)

    @staticmethod
    def info():               
        return "Area = pi * r^2"

c = Circle(3)
print(c.area())             
u = Circle.unit_circle()
print(u.radius)             
print(Circle.info())        
