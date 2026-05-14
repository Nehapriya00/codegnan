#operators

#Arthmetic
'''
print(4*6)
print(10%5==0)
print(2**5)
print(5%25==0)
print(35.20//5)

'''

#Assignment
'''
count=0
for j in range(1,10):
    count+=1
    print(count)
'''

#comparision
'''
a=7
b=9
print(a==b)

a=9
b=5
print(a!=b)

'''
#Identity
'''
a=[1,2]
b=[1,2]
c=a
print(a==b)
print(id(a))
print(id(b))
print(id(c))
print(a is b)
print(a is c)
print(a is not b)
'''
#logical
'''
a=5
if a%5==0 and a%5==0:
    print("True")

a=5
if a%3==0 or a%5==0:
    print("true")
'''
#membership
'''
a=7
b=[1,2,7,8]
print (a in b)

#bitwise
print(5|3)
'''
#methods
#replace()
any="python is a language"
print(any.replace("python","java"))
print(any)

#split()
any="python is a language"
print(any.split("an"))
#len()
print(len(any))
#slicing()
print(any[4:13])
#indexing
print(any[13])
print(any.index("is"))


