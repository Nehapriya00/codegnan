#Polumorphism: this means "many form" it allows the same function, method ,or operator to behave differently depending on object.
#1.Method Overloading:it means defining multiple methods with the same name but different parameters.
'''
class calculator:
    def add(self,a,b,c=0):
        return a+b+c
An=calculator()
print(An.add(3,4))
print(An.add(3,4,1))

###
class calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
        return a+b+c
An=calculator()
print(An.add(3,4))
print(An.add(3,4,1))



#2.Method Overriding:this occurs when a child class provides its own implementation of a method already defined in the parent class.
class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("DOG Barks")
nt=dog()
nt.sound()



#3.Operator Overloading: this operator overloading allows operators such as +,-,* etc, to perfor different actions for user-defined objects.

class std:
    def __init__(self,marks):
        self.marks=marks
    def __add__(self,other):
        return self.marks+other.marks
so1=std(4)
so=std(10)
print(so1+so)

class add:
    def sub(self,a,c,b=0):
        return a-b-c
a=add()
print(a.sub(3,6))
print(a.sub(3,12,5))

class emp:
    def id(self):
        print("my id is 6743")
class std:
    def id(self):
        print("std has another id")
g=std()
g.id()
'''

#Abstraction: this is the process of hiding internal implementation details on showing only essential features to the user.
#it focuses on what an object does rather than how it does it.
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    def perimeters(self):
        pass
class Rec(shape):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        return self.a*self.b
    def perimeters(self):
        return 2*(self.a*self.b)
an=Rec(10,5)
print(an.area())
