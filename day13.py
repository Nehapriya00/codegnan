'''
#fibnaaci
num=0
num2=1
def fib(num,num2):
    limit=int(input("Enter the limit:"))
    print(num,num2,end=" ")
    for i in range(1,limit):
        num3=num+num2
        num=num2
        num2=num3
        print(num3,end=" ")
fib(num,num2)

#program to remove duplicates
n = [2,5,7,9,2,7]
new=[]
def dup(n,new):
    for j in n:
        if j not in new:
            new.append(j)
    print(new)
dup(n,new)


#program to print number of words in a string
count=0
a="Success comes from consistent effort, not just talent".split()
def word(a,count):
    for i in a:
        count+=1
    print(count)
word(a,count)
'''
