'''
#List Comprehension : this list comprehension offers syntax when we want to create new list from existing list
#syntax:variable_name=[expression loop condition]
old=[2,3,4,5,6]
new=[so for so in old]
print(new)

#print only even numbers
old=[2,3,4,5,6]
new=[so for so in old if so%2==0]
print(new)

#print even in even nos place and print list same
old=[2,3,4,5,6]
new=[so if so%2!=0 else "even" for so in old]
print(new)


#Generators: Generators in python are a special type of itterable,allowing users to iterate over data efficiently without storing everything in memory.
#They generate values lazily using yield keyword
#Why to use generators: Generators does not store the entire dataset in memory,they genrate values on the fly or runtime.
#to avoid unnecessary storage of data speed up execution.
#how it works: it look like normal function but uses the yield keyword instead of return
#when the function is called it does not execute immediately.Instead,it return a generator object which can be iterated using loop or the next() function.
def simple_gen():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("end")
gen=simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

#program
def any(num):
    for i in range(num):
        yield i*i
a=any(5)
print(next(a))
print(next(a))
print(next(a))
print(next(a))


#program
def sqr(num):
    result=[]
    for i in range(1,num+1):
        result.append(i*i)
    return result
print(sqr(5))
'''

#program to print only consonents in a string
so="Success comes from consistent effort, not just talent"
any=''
for j in so:
    if  j not in 'AEIOUaeiou':
        any+=j
print(any)

