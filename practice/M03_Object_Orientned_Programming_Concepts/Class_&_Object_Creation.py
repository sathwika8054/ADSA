class Example:
    x=100
    def display(self):
        print("This is Example class display method")
obj=Example()
print(obj.x)
obj.display()

#create class circle using 2 methods Area and perimeter
from math import pi
class Circle:
    r=int(input())
    def area(self):
        print(pi*self.r*self.r)
    def primeter(self):
        print(2*pi*self.r)
ob=Circle()
ob.area()
ob.primeter()

