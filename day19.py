#inheritance : this allows one class to aquire the properties and methods of another class.
#Types: 1.single, 2.mutliple, 3.mutli-level, 4.hierarchical ,5.hybrid

#1.Single Inheritance: a class inherit from a single parent class
class father:
    def Land(self):
        print("My father has 10A")
class Neha(father):
    def myown(self):
        print("I own 5A")
fam=Neha()
fam.Land()


#2.Multiple Inheritance: a class inherit from more than one parent class
class father:
    def Land(self):
        print("My father has 10A")
class mother:
    def gold(self):
        print("My mother has 1 kg gold")
class Neha(father,mother):
    def myown(self):
        print("I have ntg")
fam=Neha()
fam.Land()
fam.gold()


#3.Multi-level Inheritance: a class inherit from a parent class and another class inherits from that child class
class grandfather:
    def land(self):
        print("My grand father have 5A")
class father(grandfather):
    def flat(self):
        print("My father has 1 flat")
class son(father):
    def ntg(self):
        print("I own the both p")

a=son()
a.land()
a.flat()
a.ntg()


#4.Hierarchical Inheritance: multiple child classs inherit from a single parent
class father:
    def land(self):
        print("my father has 10A")
class son(father):
    def m(self):
        print("job")
class son2(father):
    def n(self):
        print("jobless")
s=son2()
s.n()
a=son()
a.m()


#5.Hybrid Inheritance: this is the combination of two or more types of inheritance
class A:
    def some(self):
        print("CLASS A")
class B(A):
    def any(self):
        print("CLASS B")
class C(A):
    def so(self):
        print("CLASS C")
class D(B,C):
    def an(self):
        print("CLASS D")
e=D()
e.an()
e.so()

 
#super method: it is used to access methods and constructor of the parent class from the child class
class parent:
    def display(self):
        print("method parent")
class child(parent):
    def display(self):
        super().display()
        print("method child")
any=child()
any.display()
 

#program
class person:
    def __init__(self,name):
        self.name=name
class std(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def show(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll}")
any=std("priya",12)
any.show()
        
