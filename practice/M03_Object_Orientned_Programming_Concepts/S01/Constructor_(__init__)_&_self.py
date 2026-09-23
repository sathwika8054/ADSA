class A:
    count=0
    def __init__(self):
        A.count+=1

a=A()
b=A()
c=A()
print("Object count is:",A.count)


from math import pi
class Circle:
    def __init__(self,r):
        self.r=r
    def area(self):
        return pi*self.r*self.r
    def perimeter(self):
        return 2*pi*self.r
c=Circle(4)
c1=Circle(3)
c2=Circle(7)
print(c.area())
print(c.perimeter())
print(c1.area())
print(c1.perimeter())
print(c2.area())
print(c2.perimeter())

#1603
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.slots=[0,big,medium,small]
    def addCar(self, carType: int) -> bool:
        if self.slots[carType]>0:
            self.slots[carType]-=1
            return True
        return False

