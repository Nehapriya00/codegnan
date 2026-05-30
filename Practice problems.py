'''
#program to find amstrong number using functions
def how(num):
    count=0
    n=len(str(num))
    for d in str(num):
        count+=int(d)**n
    if count==num:
        print("amstrong")
    else:
        print(" not amstrong")
num=int(input("Enter a number:"))
how(num)


#program to find palindrome number using function
def how(so):
    empty=" "
    for j in so:
        empty=j+empty
        print(empty)
    if empty==0:
        print("palindrome")
    else:
        print("not palindrome")
so=input("enter string:")
how(so)
  

#program to find perfect number using function
def how(num):
    per=0
    for i in range(1,num):
        if num%i==0:
            per+=i
    if per==num:
        print(f"{num} is a perfect number")
    else:
        print(f"{num} is not a perfect number")
num=int(input("enter number:"))
how(num)


#program to find prime numbers using function
def check(num):
    count=0
    for j in range(1,num+1):
        if num%j==0:
            count+=1
        
    if count==2:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")
check(19)


#program to print * pattern
def star(a):    
    for g in range(1, a + 1):
        for i in range(1, g + 1):
            print("*", end=" ")
        print()

star(5)


#program to print alphabets pattern using function
def alphabet(star):
    for g in range(1,star+1):
        for n in range(1,g+1):
            print(chr(64+n), end=" ")
        print()
alphabet(5)


#program to print numbers pattern using function
def alphabet(star):
    count=0
    for h in range(1,star+1):
        for a in range(1,h+1):
            count+=1
            print(a , end=" ")
        print()
alphabet(7)


#program to print * in reverse pattern using function
def pa(star):
    count=0
    for g in range(star,0,-1):
        for d in range(g):
            print("*", end=" ")
        print()
pa(5)


#program to print alphabets in reverse pattern using function
def alpha(start):
    count=0
    for g in range(start,0,-1):
        for d in range(1,g+1):
            print(chr(64+d),end=" ")
        print()
alpha(6)

#program for pyramid pattern using function
def py(num):
    for j in range(1,num+1):
        print(" "*(num-j),end=" ")
        for i in range(1,j+1):
            print("*",end=" ")
        print()
py(5)

#nested loops using function
def num():
    for i in range(1,10):
        for j in range(1,3):
            print(i)
            print(j)
num()


#program for tables using function
def print_table(num):
    for j in range(1, 11):
        print(f"{num} x {j} = {num * j}")
num = int(input("Enter which table you want: "))
print_table(num)


#program to find grade using function
def grade(std_marks):
    if std_marks >= 90:
        print("A+")
    elif std_marks >= 80:
        print("A")
    elif std_marks >= 70:
        print("B+")
    elif std_marks >= 60:
        print("B")
    elif std_marks >= 50:
        print("C+")
    elif std_marks >= 35:
        print("Pass")
    else:
        print("Fail")
grade(89)


#program to find the maximum number out of 3 numbers using function
def max(num1,num2,num3):
    if num1>num2 & num1>num3:
        print(num1)
    elif num2>num1 & num2>num3:
        print(num2)
    else:
        print(num3)
max(45,65,87)


#nested if: it is defined as if inside if is called nested if using function
def check_pin():
    SBI_bank={"ATM PIN":"7798"}
    pin=input("enter 4 digit ATM Pin:")
    if len(pin)==4:
        if pin in SBI_bank['ATM PIN']:
            print("Welcome to SBI ATM")
        else:
            print("Invalid Pin")
    else:
        print("correctly enter 4 digit number")
check_pin()


# program
def elements():
    an = "python"
    ik = [5, 6, 7]
    so = (2, 3, 4)
    
    for j in ik:
        print(j)
elements()


#program
def numbers():
    for i in range(50, 100, 3):
        print(i)
    else:
        print("code ended here")
numbers()


#program
def five():
    for i in range(1,10):
        print(i)
        if i==5:
        
            break
five()
'''

#program
def the():
    for i in range(2,8):
        if i==5:
            continue
        print(i)
the()

#program
def p():
    for i in range(1,10):
        if i==3:
            pass
        print(i)
p()
