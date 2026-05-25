
#assert : this is debugging statement. It is used to check whether a condition is true . If the condition is ot true it show error as AssertionError
num=15
assert num>25
print("true")


#
age=21
assert age>18,"Age must me greater than or equal to 18"
print("Eligible")



#functions : A function is a block of code which only execute when it is called. We can pass data known as parameters into a function.
#To avoid repeated lines in code
#def function_name(parameters): this line is called definition of function
#function_name(arguments): this line is called calling function

#basic program on functiond
num=9
def even(num):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(num)
even(204)


#ways to pass arguments
#1.Required arguments: a function must be called with the same no of arguments
def even(num,num2):
    if num%2==0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
even(20,24)

#2.Default arguments : it take by default arguments values
def how(name="neha",age=21,salary=50000):
    print(name)
    print(age)
    print(salary)
how("priya",22,55000)


#3.Keyword arguments: we can send arguments with key=value syntax.By this,the order of arguments does not matter
def how(name,salary,age):
    print(name)
    print(age)
    print(salary)
how(name="priya",age=21,salary=55000)


#4.variable length arguments: adding a star(*) before the parameter name in the function, receive a tuple of arguments and can access items with index.
def hat(*name):
    print(name[2])
hat("orange","apple","kiwi","grapes","mango")


#5.passing by value:
def the(name):
    print(name)
the("apple")


#6.passing by reference:
name="kiwi"
def the(any):
    print(name)
the(name)



