'''
#concatination : the (+)for int is addition,but for other data types it will act as concatination the data type
a=90
b=8
print(a+b)
any_="python "
so="is a language"
print(any_+so)
an=[1,2]
am=[3,4]
print(an+am)


#tuple : collection of different data types seperated by commas,represented by () and it is immutable
#methods
#count() : this is used to count the particular item in the tuple
#syntax:variable_name.count(item)
some=(1,"python",[1,2],(3,4))
print(some)
print(some.count("python"))

#index():used to find out index position of the item, and only gives the first occurance 
#syntax: variable_name.index(item)
some=(1,[1,2],(3,4),"python")
print(some.index("python"))

any=(1,"python",(1,2,[34,"this is python 3rd class",78],"python is a language",89),[3,4])

print(any[2])
print(any[2][2][2])

#Dictionary : dict is key : value pair seperated by coloun: and pair is seperated by comma
#represented by {}
neha_details={"Name":"Neha",1:2,(1,2):[3,4]}
print(neha_details)

#methods
#syntax: dict.key()
neha_details={"Name":"Neha","age":21,"mobN": 3336669992,"pan":"HJONX78H"}
print(neha_details.keys())


#values(): it is used to get all the values from dict
#syntax: dict.values()
neha_details={"Name":"Neha","age":21,"mobN": 3336669992,"pan":"HJONX78H"}
print(neha_details.values())

#items(): it is used to get key and values together
#syntax:dict.items()
neha_details={"Name":"Neha","age":21,"mobN": 3336669992,"pan":"HJONX78H"}
print(neha_details.items())


#when we call key we should get the value of that key
neha_details={"Name":"Neha","age":21,"mobN": 3336669992,"pan":"HJONX78H"}
print(neha_details["Name"])
print(neha_details["pan"])


#methods
#update():used to add new key: value pair into dict
#syntax: dict.uptade({key:value})
neha_details={"Name":"Neha","age":21,"mobN": 3336669992,"pan":"HJONX78H"}
neha_details.update({"Aadhar":"784513555587"})
neha_details['Name']="Priya"
print(neha_details)
'''

#clear(): it is used to remove all the items in the dict
#syntax:variable_name.clear()
neha_details={"Name":"Neha","age":21,"mobN": 3336669992,"pan":"HJONX78H"}
neha_details.clear()
print(neha_details)
