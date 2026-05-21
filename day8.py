
#elif : it is defined as we will fetch for more items
#programs
std_marks=89
if std_marks>=90:
    print("A+")
elif std_marks>=80:
    print("A")
elif std_marks>=70:
    print("B+")
elif std_marks>=60:
    print("B")
elif std_marks>=50:
    print("C+")
elif std_marks>=35:
    print("Pass")
else:
    print("Fail")

#program to find the maximum number out of 3 numbers
num1=25
num2=12
num3=89
if num1>num2 & num1>num3:
    print(num1)
elif num2>num1 & num2>num3:
    print(num2)
else:
    print(num3)
 

#nested if: it is defined as if inside if is called nested if
SBI_bank={"ATM PIN":"7798"}
pin=input("enter 4 digit ATM Pin:")
if len(pin)==4:
    if pin in SBI_bank['ATM PIN']:
        print("Welcome to SBI ATM")
    else:
        print("Invalid Pin")
else:
    print("correctly enter 4 digit number")



#for statement: used to itterate over a square
#the variable in for loop is known as initial variable or instance variable (eg:j in for). 
an="python"
ik=[5,6,7]
so=(2,3,4)
for j in ik:
    print(j)

#range():range is a inbuilt function used to generate numbers in sequance manner
#syntax: range(start,end,step)
#else in for : once the itterasions completed this else will be executed
for i in range(50,100,3):
    print(i)
else:
    print("code ended here")


#break: used to exit from the loop based on the condition
for i in range(1,10):
    print(i)
    if i==5:
        
        break

#continue: used to skip the current itteration base on the condition
for i in range(2,8):
    if i==5:
        continue
    print(i)

#pass
for i in range(1,10):
    if i==3:
        pass
    print(i)

#while : it is the combination of for and if conditions
i=1
while i<5:
    print(i)
    i+=1
