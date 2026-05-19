
#type conversions : converting one datatype to another data type
#int
an=98
ha=str(an)
th=float(an)
print(type(ha))
print(type(th))
print(ha)
print(th)

#string
an="76"
num=int(an)
print(type(num))

#we cannot convert char to int.we can only convert int values which is in double " " in a string.
an="Python"
num=int(an)
print(type(num))

an="76"
num=list(an)
print(type(num))
print(num)
test=tuple(an)
print(type(test))
print(test)

#float
an=89.76
go=int(an)
print(type(go))
print(go)
print(type(str(an)))
for j in str(an):
    print(j)

#list
an=[6,8]
print(str(an))
for j in str(an):
    print(j)
print(tuple(an))

#tuple
ab=(3,6)
print(list(ab))
print(str(ab))

#int as user-input
num=int(input("enter number:"))
print(67+num)

#str as user-input
some=input("write text here:")
print (some)

any=list(map(int,input("enter number:").split()))
print(any)

an=tuple(map(int,input("enter numbers:").split()))
print(an)

#eval: it will print which data type is the given values
num=eval(input("enter values:"))
print(type(num))
