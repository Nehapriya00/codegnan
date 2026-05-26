'''
#Built-in function: it is know as already pre- defined
#eg:input(),len(),print(),pop(),min(),max(),type()
#sort and sorted: sort will sort the values perminently while sorted will sort in run-time it will not sort ppermenently
n=[4,6,2,3]
print(sorted(n))
print(n)

#using sort example
n=[6,3,4,1]
n.sort()
print(n)


#Recurcive function : a recurcive function that calls itself to solve a problem by breaking it into small or simple su problems.
def fac(num):
    if num==1:
        return 1
    return num*fac(num-1)
print(fac(6))


#return: this ends a function execution and sends a value back to the code that called the fuction
def add(a,b):
    return a+b
result=add(4,5)
print(result)


#lambda functions: a lambda function is a small anonamus functions. it is also known as single line expression.
#lambda can take n number of arguments,but only one expression
#syntax:lambda arguments:expression
so=lambda a,b,c:a+b+c
print(so(3,6,4))

#
so=lambda a,b,c:a-b-c
print(so(9,6,2))

#
so=lambda a,d,h:a*d*h
print(so(5,8,2))




