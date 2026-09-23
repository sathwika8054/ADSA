#isinstance checking
#isinstance()
print(type(10))
print(type(8.98))
print(type(4.99999999999999999))
print(type([1,3,4,5,5,7,8,8]))
print(type({1,2,3}))
print(type({"name" : "sathwika"}))

'''isinstance: to check weather the value/object is belong to the particular class or datatype
syntax:
isinstance(obj,isinstance)
output:
bollean 
True/False'''
print(isinstance(10,int))
print(isinstance(8.98,float))
print(isinstance(4.99999999999999999,float))
print(isinstance([1,3,4,5,5,7,8,8],list))
print(isinstance({1,2,3},tuple))
print(isinstance({"name" : "sathwika"},dict))

x="ram"
if isinstance(x,(int,float)):
    print("Given x in int or float") #same value with multiple datatypes
else:
    print("Given x is string")
#checking with classes
class animal:
    pass
class dog(animal):
    pass
a=dog()
print(isinstance(a,dog))
print(isinstance(a,animal))
#duck typing: same method acts as same behavior ,we can use it
class dog:
    def sound(self):
        print("Bow Bow")
class cat:
    def sound(self):
        print("meow meow")
def make_sound(animal):
    animal.sound()
d=dog()
c=cat()
make_sound(d)
make_sound(c)
#example
class a:
    pass 
class b(a):
    pass
obj=b()
print(type(obj)==b)
print(type(obj)==a)
print(isinstance(obj,b))
print(isinstance(obj,a))


