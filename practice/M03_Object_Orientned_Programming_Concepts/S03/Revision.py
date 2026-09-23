#single inheritence
class car:
    def brand(self):
        print("BMW")
class bike(car):
    def kmph(self):
        print(40)
a=bike()
a.kmph()
a.brand()
#multiple inheritence
class father():
    def smart(self):
        print("studying skills")
class mother():
    def cooking(self):
        print("cokking skilss")
class child(father,mother):
    def skills(self):
        print("Super")
a=child()
a.cooking()
a.smart()
a.skills()
#multilevel inheritence
class parent():
    def skills(self):
        print("smart")
        print("programming skills")
        print("communication skills")
class child1(parent):
    pass
class child2(parent):
    pass
a=child1()
b=child2()
a.skills()
b.skills()
#hireacheal inheritence
class grandfather():
    def characteristics(self):
        print("smart")
        print("handsome")
        print("very tall")
        print("inttelegent")
class father(grandfather):
    pass
class child(father):
    pass
a=child()
a.characteristics()
#hybrid inherentence
class father():
    def characteristics(self):
        print("smart")
        print("handsome")
        print("very tall")
        print("inttelegent")
class child(father):
    def super(self):
        print("Super")

class child1(child1,father):
    pass
a=child1()
b=child()
a.characteristics()
b.super()
