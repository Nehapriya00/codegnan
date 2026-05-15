'''
#program to convert 24hours clock to normal clock
time_="20:37"
parts_=time_.split(":")
hour_=int(parts_[0])
min_=int(parts_[1])
print(f"{time_}is converted into {hour_ -12}:{min_}pm")


#input from user

time_=input("enter 24 hours time")
parts_=time_.split(":")
hour_=int(parts_[0])
min_=int(parts_[1])
print(f"{time_}is converted into {hour_ -12}:{min_}pm")


#list
#it is the collection of different datatypes.It is represented in square brackets [] and seperated by commas, it is mutable.

any=[1,"python",[1,2,[34,"this is python 3rd class",78],"python is a language",89],[3,4]]

print(any[2][2][1][8])
print(any[2][2][2])


#methods
#append()  :this method is used to add new item into list,and it will add in the last index position.
#syntax- variable_name.append(item)
any=[1,2,3]
any.append(6)
print(any)
any.append([10,15])
print(any)

#extend(): this method is used to add itterable into list,and it will add in the last position,each value or substring is each index in the list
#syntax-variable_name.extend(itterable)
any=[1,2,3]
any.extend([6,7])
print(any)

#Immutable : could not able to modify on that particular variable eg.int,string
#Mutable : can able to modify directly on that particular variable eg.list
so="python is a language"
print(so.replace("python","java"))
print(so)
any=[1,2,3]
print(any.append(6))
print(any)
'''

#pop(): used to remove the item from the list,but will mention here index position in the pop method
#syntax: variable_name.pop(index_position)
any=[1,3,5]
print(any.pop(1))
print(any)

#remove(): used to remove the item from list,but it will take direct number not the index position
#syntax:variable_name.remove(value)
any=[1,3,5]
any.remove(3)
print(any)


