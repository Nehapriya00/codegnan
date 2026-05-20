
#fstring
num=10
if num%2==0:
    print(f"{num}is a even number")   

#condition statments : if,nested if,elif
#if : to check the statement is true or false
num=4
if num%2==0:
    print("even")
else:
    print("odd")

#if-else : else in the if statement,incase the codition becomes false then it will enter into fall-back(else),it will execute whatever inside it

num=int(input("enter the number"))
if num%2!=0:
    print(f"{num}is odd")
else:
    print(f"{num} is even")

#programs using if else
#program for voting using if else statement
age=int(input("enter your age:"))
if age>=18:
    print("you are eligible to vote")
else:
    print(f"you have to wait{18-age}more years to vote")


#program for finding greater number
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if num1>=num2:
    print(f"{num1}is greater than {num2}")
else:
    print(f"{num2}is greater than{num1}")


#program to find leap year
year=int(input("enter year:"))
if(year%4==0and year%100!=0)or year%400==0:
    print(f"{year} is leap year")
else:
    print(f"{year} is not a leap year")


#program to find vowels
vowel=input("enter letter:")
if vowel in "AEIOUaeiou":
    print(f"{vowel} is a vowel")
else:
    print(f"{vowel} is consonet")


#program to find positive number
num=int(input("enter number"))
if num>=0:
    print(f"{num}is a positive number")
else:
    print(f"{num}is a negative number")


#program to find pass or fail
marks=int(input("enter your marks:"))
std_name=input("enter your name:")
if marks>=45:
    print(f"{std_name} your pass")
else:
    print(f"{std_name} your fail")


#program to find divisibility
num=75
if num%3==0 and num%5==0:
    print(f"{num} is divisible by 3 and 5")
else:
    print(f"{num} is not divisible by 3 and 5")

#program for traffic lights
signal=int(input("1.Red, 2.Green:"))
if signal==1:
    print("you have to stop")
else:
    print("you can go")

