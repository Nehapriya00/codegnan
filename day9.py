
#nested loops
for i in range(1,10):
    for j in range(1,3):
        print(i)
        print(j)


#program for tables
num=int(input("Enter which table you want:"))
for j in range(1,11):
    print(f"{num}x{j}={num*j}")

# program to reverse a string(in-built method)
so="python"
print(so[::-1])


#program to reverse a string
so=input("enter a string:")
empty=""
for j in so:
    empty=j+empty
    print(empty)
if empty==so:
    print(f"{so} is a palindrome")
else:
    print(f"{so} is not a palindrome")



#program for amstrong number
num = int(input())

sum = 0
n = len(str(num))

for digit in str(num):
    sum += int(digit) ** n

if sum == num:
    print("Armstrong")
else:
    print("Not Armstrong")


#program for perfect number(wrong)
num=int(input("enter a number:"))
per=0
for i in range(1,num):
    if num%i==0:
        per+=i
if per==num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")


# program for prime number
num=19
count=0
for j in range(1,num+1):
    if num%j==0:
        count+=1
        
if count==2:
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


#program to print * pattern
star=5
for g in range(1,star+1):
    for a in range(1,g+1):
        print("*" ,end="")
    print()


#program to print alphabets pattern
star=5
for g in range(1,star+1):
    for n in range(1,g+1):
        print(chr(64+n), end=" ")
    print()


#program to print numbers pattern
star=7
count=0
for h in range(1,star+1):
    for a in range(1,h+1):
        count+=1
        print(a , end=" ")
    print()


#program to print * in reverse pattern
star=5
count=0
for g in range(star,0,-1):
    for d in range(g):
        print("*", end=" ")
    print()

#program to print alphabets in reverse pattern
start=5
count=0
for g in range(start,0,-1):
    for d in range(1,g+1):
        print(chr(64+d),end=" ")
    print()


#program for pyramid pattern
num=5
for j in range(1,num+1):
    print(" "*(num-j),end=" ")
    for i in range(1,j+1):
        print("*",end=" ")
    print()




