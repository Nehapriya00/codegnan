#OOPs- object oriented programming system

#1.class : a class is a blueprint or a template used to create object
#syntax: class class_name:
class std:
    def edu(self):
        print("I am studing Btech")
    def sports(self):
        print("cricket")
        
s1=std()
s1.edu()
s1.sports()

#2.object : an object is an instance of a class
class std:
    name='neha'
s1=std()
print(s1.name)


#Attributes: Attributes are the variables that belongs to a class or an object
class std:
    name='neha'
    age=21
s1=std()
print(s1.name)
print(s1.age)


#methods: the functions defined inside the class is called methods
class PFS_DA:
    def python(self):
        PFS_DA='Batch_03'
        print('This is pfs and da batch 03')
    def flask(self):
        PFS='Batch_03'
        print('This pfs batch 03')
all =PFS_DA()
all.python()
all.flask()


#constructor: (__init__)
class ATM:
    def __init__(self,Balance,name):
        self.Balance=Balance
        self.name=name
    def Bal_check(self):
        print(f"{self.name} your total balance is {self.Balance+7000}")
    def name_(self):
        print(self.name)
card=ATM(Balance=5000,name='neha')
card.Bal_check()
card.name_()


#Access Specifier: 1.public , 2.protected , 3.private
#public: this can be accessed from any way in the program
class stu:
    name='neha'
s1=stu()
print(s1.name)

#protected: this is represented using a single underscore(_)
class stu:
    _name='neha'
s1=stu()
print(s1._name)

#private: this is represented using double underscore(__)
class stu:
    __name='neha'
s1=stu()
print(s1._stu__name)


#Encapusulation: It is the process of binding data and methods together
class Bank:
    def __init__(self,balance):
        self._balance=balance
    def depo_(self,amount):
        self._balance += amount
    def get_bala(self):
        return self._balance
acc=Bank(2000)
acc.depo_(50000)
print(acc.get_bala())
