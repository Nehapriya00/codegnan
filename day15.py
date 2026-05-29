
#modules: A modules in python is a file that contains python code such as variables,functions,classes,statements.
#this are two types of modules they are user-defined,built-in.
#user-defined
def add(a,b):
    return a+b
def sub(a,b):
    return a-b


#built-in
import math
print(math.sqrt(25))
print(math.factorial(10))
print(math.pow(2,5))

#program
from math import sqrt
print(sqrt(49))


#program
import math as m
print(m.sqrt(25))
print(m.factorial(5))


#program
import os
os.remove("day3.txt")
    

#program
import sys
print(sys.version)
print(sys.exit)
print(sys.path)


#program
import random
print(random.randint(1000,9999))

#program
from collections import Counter
data=['a','b','c','d']
counter=Counter(data)
print(counter)


#program
from collections import Counter,defaultdict
data=['a','b','c','d']
counter=Counter(data)
print(counter)
ss=defaultdict(int)
ss['missing']+=1
print(ss['missing'])
print(ss)
