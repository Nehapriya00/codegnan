'''
#Write a function to calculate the area of a circle given its radius
def radius(num):
    area=3.14*num*num
    return area
r=int(input("Enter radius:"))
print("Area=",radius(r))

#Create a function to check if a number is prime
def check(num):
    for i in range(2,num):
        if i%num==0:
            return "Not prime"
    return "Prime"
num=int(input("Enter Value:"))
print(check(num))

#Implement a function that reverses a given string
def reverse(s):
    rev=" "
    for char in s:
        rev=char+rev
    return rev
s=input("Enter String:")
print(reverse(s))

#Given a list of numbers, create a function to find the sum of all positive numbers
def sum(num):
    total=0
    for i in num:
        if i>=0:
            total+=i
    return total
num=list(map(int,input("enter:").split()))
result=sum(num)
print(result)

#Write a Python function to check if a given string is a palindrome
def palin(s):
    rev=""
    for i in s:
        rev=i+rev
    if s==rev:
        return "Palindrome"
    else:
        return "Not Palindrome"
s=input("Enter string:")
print(palin(s))

#Implement a function that returns the factorial of a given number using recursion
def fac(n):
    if n<0:
        return "Not factorial it is not positive number"
    elif n==0 or n==1:
        return 1
    else:
        return n*fac(n-1)
num=int(input("enter:"))
print(fac(num))

#Create a function to find the square of each element in a given list
def square(num):
    result=[]
    for i in num:
        result.append(i**2)
    return result
num=list(map(int,input("enter:").split()))
print(square(num))

#Write a function to check if a number is even or odd and return "Even" or "Odd" accordingly
def out(num):
    even=[]
    odd=[]
    for i in num:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return even,odd
num=list(map(int,input("enter:").split()))
even,odd=out(num)
print(even)
print(odd)


#Calculate the area of a triangle given its base and height using a function
def triangle(base,height):
    return 0.5*base*height
b=int(input("enter:"))
h=int(input("enter:"))
print(triangle(b,h))


#Create a function that takes a list of strings and returns the list sorted alphabetically
def sort(num):
    return sorted(num)
words=input("enter:").split()
print(sort(words))


#Write a function that takes two lists and returns their intersection (common elements)
def intersection(list1,list2):
    result=[]
    for i in list1:
        if i in list2 and i not in result:
            result.append(i)
    return result
list1=list(map(int,input("enter:").split()))
list2=list(map(int,input("enter:").split()))
print(intersection(list1,list2))


#Implement a function to check if a given year is a leap year or not
def leap(year):
    if (year%4==0 and year%100!=0)or (year%400==0):
        return "leap year"
    else:
        return "not leap year"
year=int(input("enter:"))
print(leap(year))
'''

#Create a function that takes a number as input and prints its multiplication table.
def multi(num):
    for i in range(1,11):
        print(f"{num}x{i}={num*i}")
n=int(input("enter:"))
print(multi(n))
